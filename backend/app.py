from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI(title="Test API", version="1.0.0")

# Enable CORS for Nuxt development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Nuxt dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data models
class User(BaseModel):
    id: str
    name: str
    email: str
    created_at: str

class CreateUserRequest(BaseModel):
    name: str
    email: str

class Post(BaseModel):
    id: str
    title: str
    content: str
    author: str
    created_at: str

class CreatePostRequest(BaseModel):
    title: str
    content: str
    author: str

# In-memory storage (replace with database in production)
users_db = []
posts_db = []

# Initialize with some sample data
@app.on_event("startup")
async def startup_event():
    sample_users = [
        {"id": "1", "name": "John Doe", "email": "john@example.com", "created_at": "2024-01-15T10:30:00"},
        {"id": "2", "name": "Jane Smith", "email": "jane@example.com", "created_at": "2024-01-16T14:20:00"},
        {"id": "3", "name": "Bob Johnson", "email": "bob@example.com", "created_at": "2024-01-17T09:15:00"},
    ]
    
    sample_posts = [
        {"id": "1", "title": "First Post", "content": "This is the first post content", "author": "1", "created_at": "2024-01-18T10:00:00"},
        {"id": "2", "title": "Second Post", "content": "This is the second post content", "author": "2", "created_at": "2024-01-18T11:30:00"},
        {"id": "3", "title": "Third Post", "content": "This is the third post content", "author": "1", "created_at": "2024-01-18T12:45:00"},
    ]
    
    users_db.extend(sample_users)
    posts_db.extend(sample_posts)

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI Backend is running!", "timestamp": datetime.now().isoformat()}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# User endpoints
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

# Post endpoints
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

# Search endpoint
@app.get("/search")
async def search_posts(q: Optional[str] = None):
    if not q:
        return {"results": []}
    
    results = [p for p in posts_db if q.lower() in p["title"].lower() or q.lower() in p["content"].lower()]
    return {"query": q, "results": results, "count": len(results)}

# Error simulation endpoint
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