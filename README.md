

# PDF Content Extraction and Storage Web Application

This is a Django-based REST API web application integrated with MongoDB. It allows users to upload PDF files, extract their content (focusing on identifying nouns and verbs), and store the extracted data in a MongoDB database. The application ensures uniqueness in email addresses to avoid redundant data storage. The API provides responses with part-of-speech (POS) tags for the extracted text.

## Features

- **PDF File Upload**: Upload PDF files directly via a simple frontend form.
- **Content Extraction**: Automatically extracts text from the uploaded PDF using PyMuPDF (fitz).
- **Nouns and Verbs Extraction**: Identifies and tags nouns and verbs in the text using SpaCy.
- **Email Uniqueness**: Ensures that each uploaded file is associated with a unique email address. Duplicate emails are rejected.
- **MongoDB Integration**: Stores PDF metadata, email, and POS-tagged text in MongoDB.
- **Frontend Interface**: A simple HTML frontend for users to upload files and view the results.
- **Deployed on Vercel**: The application is deployed on Vercel for easy access and testing.

---

## Benefits

1. **Automated PDF Content Extraction**: No need to manually process large PDF files to extract content. Simply upload, and the API does the work for you.
2. **Text Analysis**: Provides basic linguistic analysis by tagging nouns and verbs, useful for further content processing or natural language processing tasks.
3. **Unique Email Validation**: Ensures that each email can only be associated with one uploaded file, preventing duplicate uploads.
4. **Scalable and Secure**: Backed by MongoDB for efficient data storage and Django for secure web operations.

---

## Technology Stack

- **Backend**: Django REST Framework (Python)
- **Database**: MongoDB
- **PDF Processing**: PyMuPDF (fitz)
- **Text Processing**: SpaCy
- **Frontend**: HTML (Bootstrap for styling)
- **Deployment**: Vercel
- **CI/CD**: GitHub Actions

---

## How to Run Locally

To run this project locally, follow the steps below.

### Prerequisites

1. **Python 3.11** installed on your system.
2. **MongoDB Atlas**: Set up a MongoDB Atlas account and get the connection string.
3. **Virtual Environment**: Recommended for isolating project dependencies.
4. **Vercel Account (for deployment)**.

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Set up a virtual environment**

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install the project dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure MongoDB**

In your Django project settings, add your MongoDB connection string.

```python
# settings.py

MONGO_CLIENT = MongoClient("your-mongodb-connection-string")
MONGO_DB = MONGO_CLIENT["your-db-name"]
MONGO_COLLECTION = MONGO_DB["your-collection-name"]
```

5. **Run the Application**

```bash
python manage.py runserver
```

6. **Test the API**

Go to `http://127.0.0.1:8000/upload/` and upload a PDF file with an email. You will see the extraction results after submission.

---

## Deployment

This application is deployed on Vercel. You can access the live version via the following link:

**[Live Application URL](https://dowell.vercel.app)**

### Steps to Deploy on Vercel:

1. **Install Vercel CLI**

```bash
npm install -g vercel
```

2. **Login to Vercel**

```bash
vercel login
```

3. **Deploy**

Inside your project directory:

```bash
vercel
```

4. **GitHub Actions CI/CD**

GitHub Actions is set up for continuous integration and deployment. Every push to the main branch will trigger an automatic deployment to Vercel.

---

## API Endpoints

### 1. Upload a PDF File
- **URL**: `/upload/`
- **Method**: POST
- **Parameters**: 
  - `file`: The PDF file to be uploaded.
  - `email`: Unique email address associated with the file.
  
- **Response**:
  - Success: `{ "message": "File processed successfully", "tags": [...] }`
  - Failure: `{ "error": "Error message" }`

---

## Future Improvements

1. **Advanced Text Analysis**: Additional NLP features like sentiment analysis or keyword extraction.
2. **File History**: Allow users to view previous uploads associated with their email.
3. **User Authentication**: Enable user accounts to track individual file submissions.
4. **Improved UI**: A more dynamic and responsive UI with real-time feedback.

---

## License

This project is licensed under the MIT License.

---

Feel free to contribute or report any issues!

