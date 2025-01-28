Here’s the README file for a YouTube Search API using Python and yt-dlp, deployed on Vercel. This service allows users to query YouTube search results and returns a JSON response with video details.


---

YouTube Search API

A lightweight API built with Python and yt-dlp to perform YouTube searches. The API fetches search results based on a query string and returns relevant video details like titles, channels, thumbnails, and video IDs. Deployed on Vercel for scalability and ease of use.


---

Features

🔍 Search YouTube Videos: Get top search results from YouTube for any query.

📦 JSON Response: Cleanly structured output with video metadata.

⚡ Serverless Deployment: Hosted on Vercel for fast, scalable, and serverless operation.

💻 Easy Integration: RESTful API suitable for various applications like video search, recommendations, or streaming.



---

API Usage

Endpoint

GET /search

Query Parameters

Example Request

GET https://ytsearch-three.vercel.app/search?query=blue

Response Format

{
  "success": true,
  "results": [
    {
      "title": "yung kai - blue (Official Music Video)",
      "channel": "yung kai",
      "video_id": "IpFX2vq8HKw",
      "thumbnail": "https://img.youtube.com/vi/IpFX2vq8HKw/hqdefault.jpg"
    },
    ...
  ]
}


---

Local Development

Getting Started

1. Clone the Repository

git clone <your-repo-url>
cd <project-directory>


2. Install Dependencies

pip install yt-dlp
pip install -r requirements.txt


3. Run the Development Server

vercel dev




---

Deployment on Vercel

Deploy in Minutes

1. Install Vercel CLI

npm install -g vercel


2. Deploy to Vercel

vercel


3. Your API will be available at:

https://<your-vercel-project>.vercel.app/search




---

Response Details

Each result contains the following details:


---

Dependencies

Python 3.9+

yt-dlp

Vercel Python Runtime



---

Error Handling

The API returns appropriate HTTP status codes:


---

Contributing

We welcome contributions! Submit issues or pull requests to enhance functionality or fix bugs.


---

License

This project is licensed under the MIT License.


---

Disclaimer

This project is not affiliated with YouTube or Google. Use this tool responsibly and ensure compliance with YouTube’s terms of service.


---

Let me know if you need help with code snippets or additional details!

