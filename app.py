from fastapi import FastAPI, Query
import yt_dlp

app = FastAPI()

def youtube_search(query):
    ydl_opts = {
        'quiet': True,
        'format': 'best',
        'noplaylist': True,
        'extract_flat': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        results = ydl.extract_info(f"ytsearch10:{query}", download=False)['entries']
        return [
            {
                "title": video['title'],
                "channel": video.get('channel', 'Unknown'),  # Extract channel name
                "video_id": video['id'],                    # Extract video ID
                "thumbnail": f"https://img.youtube.com/vi/{video['id']}/hqdefault.jpg"
            }
            for video in results
        ]

@app.get("/search")
def search(query: str = Query(..., description="Search query for YouTube")):
    try:
        results = youtube_search(query)
        return {"success": True, "results": results}
    except Exception as e:
        return {"success": False, "error": str(e)}
