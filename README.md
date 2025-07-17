# EduPlan Assistant

Transform your teaching with AI-generated lesson plans tailored to your subject, student level, and learning objectives. Save hours of planning time.

## Overview

EduPlan Assistant is an AI-powered web application that helps teachers create comprehensive, personalized lesson plans quickly and efficiently. Built with Flask and powered by OpenAI's advanced language models, it generates tailored educational content based on your specific requirements.

## Features

- **AI-Powered Generation**: Uses OpenAI's latest models to create detailed lesson plans
- **Customizable Parameters**: Specify subject, grade level, duration, focus areas, and special requirements
- **Professional Interface**: Modern, responsive design with glassmorphism styling
- **Real-time Generation**: Fast lesson plan creation with loading indicators
- **Form Validation**: Built-in validation to ensure all required fields are completed

## Getting Started

### Prerequisites

- Python 3.7+
- OpenAI API key
- Flask and required dependencies

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/teacher-ai-helper.git
cd teacher-ai-helper
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_PROMPT_ID=your_prompt_id_here
OPENAI_PROMPT_VERSION=your_prompt_version_here
```

4. Run the application:
```bash
python app.py
```

## Usage

1. Fill in the lesson plan parameters:
   - Subject and specialty area
   - Grade level (K-12)
   - Duration (hours per day, number of weeks)
   - State/region for curriculum alignment
   - Learning focus and objectives
   - Additional instructions

2. Click "Generate Lesson Plan" to create your AI-powered lesson plan

3. Review and customize the generated content as needed

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **AI**: OpenAI API (Responses endpoint)
- **Styling**: Modern CSS with glassmorphism effects
- **Environment**: dotenv for configuration management

## Future Enhancements

### High Priority
- [ ] **Progress Indicators**: Add step-by-step progress bars for multi-step processes
- [ ] **Save/Load Templates**: Allow users to save frequently used configurations
- [ ] **Export Options**: PDF, Word, or plain text export for lesson plans
- [ ] **History/Recent**: Show recently generated lesson plans
- [ ] **Validation**: Real-time form validation with helpful error messages

### Medium Priority
- [ ] **Dark Mode**: Toggle between light and dark themes
- [ ] **Responsive Design**: Enhanced mobile-friendly layout
- [ ] **Auto-save**: Save form data locally to prevent data loss
- [ ] **Preview Mode**: Show preview before final generation
- [ ] **Feedback System**: Allow users to rate and improve generated content

### Low Priority
- [ ] **User Authentication**: Allow users to save their lesson plans
- [ ] **Collaboration**: Share lesson plans with other teachers
- [ ] **Analytics**: Track usage patterns and popular subjects
- [ ] **Integration**: Connect with popular LMS platforms
- [ ] **Offline Mode**: Basic functionality when internet is limited

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Kevin**
- Portfolio: [kevin-homepage.s3-website-us-east-1.amazonaws.com](http://kevin-homepage.s3-website-us-east-1.amazonaws.com/)

## Acknowledgments

- OpenAI for providing the powerful language models
- Flask community for the excellent web framework
- Modern CSS techniques for the beautiful UI design

---

*Built with ❤️ for educators who want to focus more on teaching and less on planning.*