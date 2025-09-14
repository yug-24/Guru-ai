# Overview

Guru AI is a personalized learning tutor application designed specifically for rural students in India. The application provides an accessible educational platform that supports multiple languages and grade levels, offering explanations and quizzes tailored to students' needs. The system combines text and voice input capabilities to accommodate different learning preferences and accessibility requirements.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Streamlit Web Interface**: Single-page application using Streamlit for rapid prototyping and deployment
- **Interactive Components**: Form-based input system with dropdowns for grade selection (Class 5-8), subject selection (Math, Science, English, Social Studies), and language preferences (English, Hindi, Tamil, Bengali, Other)
- **Multi-modal Input**: Text input field and audio file upload functionality for voice-based queries
- **Real-time Response Display**: Immediate feedback and content rendering within the web interface

## Backend Architecture
- **Python-based Processing**: Single-file architecture using main.py as the entry point
- **Stateless Design**: No persistent data storage, processing requests in real-time
- **Error Handling**: Basic error handling for API failures and missing configurations

## AI Integration
- **OpenAI GPT Integration**: Uses GPT-4o-mini model for cost-effective text generation
- **Whisper Speech-to-Text**: Implements OpenAI's Whisper model for audio transcription
- **Context-Aware Prompting**: Generates grade-appropriate, language-specific, and culturally relevant content for rural Indian students

## Authentication and Security
- **Environment-based API Key Management**: OpenAI API key stored in environment variables/Replit Secrets
- **Client-side Validation**: Basic input validation and error messaging

# External Dependencies

## AI Services
- **OpenAI API**: Primary dependency for both text generation (GPT-4o-mini) and speech recognition (Whisper-1)
- **API Key Management**: Requires OPENAI_API_KEY environment variable

## Python Libraries
- **Streamlit (v1.49.1)**: Web application framework for the user interface
- **OpenAI Python SDK (v1.107.2)**: Official client library for OpenAI API interactions

## Runtime Environment
- **Replit Platform**: Designed for deployment on Replit with built-in secrets management
- **Python Runtime**: Requires Python environment with pip package management

## Audio Processing
- **Built-in IO Module**: Uses Python's io module for audio file handling
- **Supported Audio Formats**: WAV, MP3, M4A file formats for voice input