from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional

app = FastAPI()

# Dummy image data (replace with your actual image data)
image_data = {
    "cat": ["cat1.jpg", "cat2.avif"],
    "dog": ["dog1.jpg", "dog2.jpg"],
    # Add more keywords and corresponding image filenames here
}

# Dummy function to match images based on keyword (replace with actual implementation)
def match_images(keyword: str) -> List[str]:
    if keyword in image_data:
        return image_data[keyword]
    else:
        return []

@app.get("/search")
async def search_images(keyword: Optional[str] = Query(None, min_length=1)):
    if not keyword:
        raise HTTPException(status_code=400, detail="Keyword parameter is required")
    
    matched_images = match_images(keyword)
    if matched_images:
        return {"images": matched_images}
    else:
        return {"message": f"No matching images found for keyword '{keyword}'"}

@app.get("/")
async def root():
    return {"message": "Hello World"}
