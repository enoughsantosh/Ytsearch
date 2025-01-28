# YouTube Search API

A lightweight API built with Python and yt-dlp to perform YouTube searches. This service allows users to query YouTube search results and returns structured JSON responses with comprehensive video details. Deployed on Vercel for scalable, serverless operations.

## 🌟 Features

- **Powerful Search**: Retrieve top YouTube search results with detailed metadata
- **JSON Response Format**: Clean, well-structured output for easy integration
- **Serverless Architecture**: Leverages Vercel for reliable, scalable deployment
- **Low Latency**: Optimized for quick response times
- **Cross-Platform Compatible**: RESTful API design works with any platform or language

## 📚 API Documentation

### Base URL
```
https://ytsearch-three.vercel.app
```

### Endpoints

#### Search Videos
```http
GET /search
```

##### Query Parameters
| Parameter | Type   | Required | Description                                      |
|-----------|--------|----------|--------------------------------------------------|
| query     | string | Yes      | Search term for YouTube videos                   |
| limit     | number | No       | Maximum number of results (default: 10, max: 50) |

##### Example Request
```http
GET https://ytsearch-three.vercel.app/search?query=blue&limit=2
```

##### Response Format
```json
{
  "success": true,
  "results": [
    {
      "title": "yung kai - blue (Official Music Video)",
      "channel": "yung kai",
      "video_id": "IpFX2vq8HKw",
      "thumbnail": "https://img.youtube.com/vi/IpFX2vq8HKw/hqdefault.jpg",
      "duration": "3:42",
      "views": "1.2M",
      "published": "2023-12-15"
    }
  ]
}
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Node.js and npm (for Vercel CLI)

### Local Development

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd youtube-search-api
   ```



2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```



3. **Run Development Server**
   ```bash
   vercel dev
   ```

## 📦 Deployment

### Deploying to Vercel

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Configure Vercel Project**
   ```bash
   vercel login
   vercel link
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

## ⚡ Response Details

Each video result includes:
- `title`: Video title
- `channel`: Channel name
- `video_id`: Unique YouTube video identifier
- `thumbnail`: High-quality thumbnail URL
- `duration`: Video length
- `views`: View count
- `published`: Publication date

## 🛠️ Error Handling

| Status Code | Description                                    |
|-------------|------------------------------------------------|
| 200         | Successful request                             |
| 400         | Bad request (invalid parameters)               |
| 429         | Rate limit exceeded                           |
| 500         | Internal server error                         |

Error Response Format:
```json
{
  "success": false,
  "error": "Error message description"
}
```


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This project is not affiliated with, endorsed by, or sponsored by YouTube or Google. Users must ensure compliance with YouTube's Terms of Service when using this API.

## 📮 Support

For issues, feature requests, or questions:
- Open an issue in the GitHub repository
  

---

Made with ❤️ 
