# EduPlan Assistant

<p align="center">
  <img src="images/kevin_logo.png" alt="Kevin's Logo" width="200" height="200">
</p>

<p align="center">
  <strong>Transform your teaching with AI-generated lesson plans tailored to your subject, student level, and learning objectives. Save hours of planning time.</strong>
</p>

<p align="center">
  <em>Created by Kevin - 8th/9th Grade Developer</em>
</p>

## Overview

EduPlan Assistant is an AI-powered web application that helps teachers create comprehensive, personalized lesson plans quickly and efficiently. Built with Flask and powered by OpenAI's advanced language models, it generates tailored educational content based on your specific requirements.

### AI Architecture: Linear LLM Approach

EduPlan Assistant utilizes a **linear LLM (Large Language Model) architecture** rather than multi-agent systems. This design choice offers several advantages for lesson planning:

**Linear Models Benefits:**
- **Simplicity**: Single-model approach reduces complexity and potential points of failure
- **Speed**: Faster processing for straightforward lesson planning tasks
- **Consistency**: Uniform output style and quality across all generated content
- **Cost-Effective**: Lower computational overhead compared to multi-agent systems
- **Reliability**: Proven stability for focused, domain-specific tasks

**When Linear vs Multi-Agent:**
- **Linear models** excel at straightforward, well-defined tasks like lesson plan generation where a single expert perspective is sufficient
- **Multi-agent systems** are better suited for complex, multifaceted problems requiring diverse expertise, parallel processing, and collaborative problem-solving

For educational content generation, the linear approach provides the optimal balance of speed, reliability, and quality that teachers need for their daily planning workflow.

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

### High Priority - AI-Enhanced Features
- [ ] **Voice Input**: Natural speech-to-text input that auto-fills form fields
- [ ] **Smart Auto-Complete**: AI-powered suggestions as users type in form fields
- [ ] **Conversational Interface**: Chat-based lesson plan creation with follow-up questions
- [ ] **Intelligent Form Pre-filling**: AI analyzes subject/grade and suggests optimal parameters
- [ ] **Content Enhancement**: AI-powered suggestions to improve generated lesson plans
- [ ] **Multi-Modal Input**: Support for image uploads (curriculum documents, worksheets) to inform lesson planning
- [ ] **Adaptive Learning**: AI learns from user preferences and improves suggestions over time
- [ ] **Real-time Collaboration**: AI-assisted collaborative lesson planning with other teachers

### High Priority - Core Features
- [ ] **Progress Indicators**: Add step-by-step progress bars for multi-step processes
- [ ] **Save/Load Templates**: Allow users to save frequently used configurations
- [ ] **Export Options**: PDF, Word, or plain text export for lesson plans
- [ ] **History/Recent**: Show recently generated lesson plans with AI-powered search
- [ ] **Validation**: Real-time form validation with helpful error messages

### Medium Priority - AI-Powered Enhancements
- [ ] **Curriculum Alignment**: AI automatically aligns lesson plans with state standards
- [ ] **Difficulty Adjustment**: AI-powered difficulty scaling based on student performance data
- [ ] **Resource Recommendations**: AI suggests relevant materials, videos, and activities
- [ ] **Assessment Generation**: Automatically create quizzes and rubrics from lesson plans
- [ ] **Personalization Engine**: AI customizes content based on teaching style and student needs
- [ ] **Language Translation**: Multi-language support for diverse classrooms
- [ ] **Accessibility Features**: AI-generated alternative formats for different learning needs

### Medium Priority - User Experience
- [ ] **Dark Mode**: Toggle between light and dark themes
- [ ] **Responsive Design**: Enhanced mobile-friendly layout
- [ ] **Auto-save**: Save form data locally to prevent data loss
- [ ] **Preview Mode**: Show preview before final generation
- [ ] **Feedback System**: Allow users to rate and improve generated content with AI learning

### Low Priority - Platform & Integration
- [ ] **User Authentication**: Allow users to save their lesson plans
- [ ] **Collaboration**: Share lesson plans with other teachers
- [ ] **Analytics**: Track usage patterns and popular subjects with AI insights
- [ ] **LMS Integration**: Connect with popular platforms (Google Classroom, Canvas, Blackboard)
- [ ] **Calendar Integration**: Sync lesson plans with teaching schedules
- [ ] **Mobile App**: Native iOS/Android app with offline AI capabilities
- [ ] **API Access**: Allow third-party integrations and custom tools

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

<p align="center">
  <img src="images/kevin_logo.png" alt="Kevin's Logo" width="100" height="100">
</p>

**Kevin** - *8th/9th Grade Developer*
- Portfolio: [kevin-homepage.s3-website-us-east-1.amazonaws.com](http://kevin-homepage.s3-website-us-east-1.amazonaws.com/)
- Age: 8th/9th Grade Student
- Skills: Python, Flask, AI Integration, Web Development, UI/UX Design

> *"Demonstrating that age is just a number when it comes to creating innovative solutions. This project showcases advanced programming skills, AI integration, and professional web development capabilities."*

## Acknowledgments

- OpenAI for providing the powerful language models
- Flask community for the excellent web framework
- Modern CSS techniques for the beautiful UI design

---

*Built with ❤️ for educators who want to focus more on teaching and less on planning.*