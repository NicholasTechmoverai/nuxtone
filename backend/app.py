from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime
from prototype_db import sample_users, sample_posts, sample_properties
from fastapi import FastAPI, Query
from fastapi import FastAPI, Body
from search import get_query_parser
import re
app = FastAPI(title="Test API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000","https://injustify.tera-in.top"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    id: str
    name: str
    email: str
    created_at: str
    role: str
    avatar: str
    bio: str
    location: str
    phone: str


class Post(BaseModel):
    id: str
    title: str
    content: str
    author: str  # user id
    created_at: str
    image: str
    category: str
    likes: int
    comments: int


class Property(BaseModel):
    id: str
    title: str
    description: str
    price: int
    location: str
    bedrooms: int
    bathrooms: int
    square_feet: int
    property_type: str
    year_built: int
    owner_id: str
    created_at: str
    image: str

class CreateUserRequest(BaseModel):
    name: str
    email: str



class CreatePostRequest(BaseModel):
    title: str
    content: str
    author: str

users_db = []
posts_db = []
property_db = []

@app.on_event("startup")
async def startup_event():
    users_db.extend(sample_users)
    posts_db.extend(sample_posts)
    property_db.extend(sample_properties)

@app.get("/")
async def root():
    return {"message": "FastAPI Backend is running!", "timestamp": datetime.now().isoformat()}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/users", response_model=List[User])
async def get_users(skip: int = 0, limit: int = 10):
    return users_db[skip:skip + limit]

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = next((u for u in users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User)
async def create_user(user: CreateUserRequest):
    new_user = {
        "id": str(uuid.uuid4()),
        "name": user.name,
        "email": user.email,
        "created_at": datetime.now().isoformat()
    }
    users_db.append(new_user)
    return new_user

@app.get("/posts", response_model=List[Post])
async def get_posts(skip: int = 0, limit: int = 10):
    return posts_db[skip:skip + limit]

@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: str):
    post = next((p for p in posts_db if p["id"] == post_id), None)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.post("/posts", response_model=Post)
async def create_post(post: CreatePostRequest):
    new_post = {
        "id": str(uuid.uuid4()),
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "created_at": datetime.now().isoformat()
    }
    posts_db.append(new_post)
    return new_post

@app.get("/search")
async def search_posts(q: Optional[str] = None):
    if not q:
        return {"results": []}
    
    results = [p for p in posts_db if q.lower() in p["title"].lower() or q.lower() in p["content"].lower()]
    return {"query": q, "results": results, "count": len(results)}


@app.get("/properties", response_model=List[Property])
async def get_properties(
    skip: int = 0, 
    limit: int = 10,
    property_type: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    bedrooms: Optional[int] = None
):
    """
    Get properties with filtering and pagination
    """
    filtered_properties = property_db
    
    # Apply filters
    if property_type:
        filtered_properties = [p for p in filtered_properties if p["property_type"].lower() == property_type.lower()]
    
    if min_price is not None:
        filtered_properties = [p for p in filtered_properties if p["price"] >= min_price]
    
    if max_price is not None:
        filtered_properties = [p for p in filtered_properties if p["price"] <= max_price]
    
    if bedrooms is not None:
        filtered_properties = [p for p in filtered_properties if p["bedrooms"] >= bedrooms]
    
    #  pagination
    return filtered_properties[skip:skip + limit]



@app.get("/properties/type/{property_type}", response_model=List[Property])
async def get_properties_by_type(property_type: str):
    """
    Get all properties of a specific type
    """
    properties = [p for p in property_db if p["property_type"].lower() == property_type.lower()]
    if not properties:
        raise HTTPException(status_code=404, detail=f"No properties found for type: {property_type}")
    return properties


@app.get("/properties/list/search")
async def search_properties(
    type: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    bedrooms: Optional[int] = Query(None),
):
    print("Handling Search", type, location, bedrooms)

    results = property_db 

    if type:
        results = [p for p in results if p["property_type"].lower() == type.lower()]
    if location:
        results = [p for p in results if location.lower() in p["location"].lower()]
    if bedrooms:
        results = [p for p in results if p["bedrooms"] == bedrooms]

    return results


from fastapi import Query, HTTPException
from typing import Optional

@app.get("/search-properties/v2/nlp-search")
async def nlp_search(query: Optional[str] = Query(None, description="NLP search query")):
    """SEO-friendly NLP search (GET)"""
    
    # Debug logging
    print(f"Received query: {query}")
    
    # Handle missing or empty query
    if not query or not query.strip():
        raise HTTPException(
            status_code=422, 
            detail="Query parameter 'q' is required and cannot be empty"
        )

    try:
        parsed = await get_query_parser(query.strip().lower())
        
        if not parsed["success"]:
            raise HTTPException(
                status_code=422, 
                detail=f"Could not understand query: {parsed.get('error', 'Unknown error')}"
            )

        entities = parsed.get("entities", {})
        matched = sample_properties.copy()

        # Apply filters
        for key, value in entities.items():
            if not value:
                continue

            if isinstance(value, list):  # amenities
                matched = [
                    p for p in matched
                    if all(
                        any(v.lower() in str(p.get(field, "")).lower() 
                            for field in ["description", "title", "amenities"])
                        for v in value
                    )
                ]
            else:  # location, property_type, bedrooms, etc.
                matched = [
                    p for p in matched
                    if str(value).lower() in str(p.get(key, "")).lower()
                ]

        return {
            "success": True,
            "query": query,
            "filters": entities,
            "results_count": len(matched),
            "properties": matched,
            "seo": {
                "title": f"Properties matching '{query}'",
                "description": f"Find properties related to: {query}",
                "image": matched[0]["image"] if matched else ""
            }
        }
        
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail="Internal server error while processing search"
        )


@app.get("/properties/owner/{owner_id}", response_model=List[Property])
async def get_properties_by_owner(owner_id: str):
    """
    Get all properties owned by a specific user
    """
    properties = [p for p in property_db if p["owner_id"] == owner_id]
    if not properties:
        raise HTTPException(status_code=404, detail=f"No properties found for owner: {owner_id}")
    return properties

@app.get("/properties/{property_id}", response_model=Property)
async def get_property(property_id: str):
    """
    Get a specific property by ID
    """
    property = next((p for p in property_db if p["id"] == property_id), None)
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property

@app.get("/simulate-error")
async def simulate_error():
    raise HTTPException(status_code=500, detail="This is a simulated server error")

# Delayed response endpoint (for testing loading states)
@app.get("/slow-data")
async def slow_data(delay: int = 2):
    import time
    time.sleep(delay)  # Simulate slow response
    return {
        "message": f"This response was delayed by {delay} seconds",
        "data": ["item1", "item2", "item3"],
        "timestamp": datetime.now().isoformat()
    }



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)