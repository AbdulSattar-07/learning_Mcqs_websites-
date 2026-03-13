# MCQ Learning Platform

A production-ready Django web application for the National Skill Competency Test for IT Graduates. This platform manages 20,000+ Multiple Choice Questions with secure access control and content protection.

## Features

### Public Access
- Browse Domains, Topics, and Subtopics
- View platform information
- Request subscription via WhatsApp integration
- Choose from 7, 15, or 30 days packages

### Paid User Access
- View and practice MCQs
- Filter by Domain, Topic, Subtopic, Batch, Difficulty, Tag
- Search MCQs by keyword
- View answers and explanations
- Paginated results (20 per page)
- Single device login enforcement

### Admin Features
- User management with subscription control
- Subscription request management with one-click approval
- Automatic username/password generation
- WhatsApp-based credential delivery workflow
- Active session monitoring and management
- Force logout capability
- MCQ management (CRUD operations)
- Bulk import from CSV/JSON
- Contact request management
- Domain/Topic/Subtopic management

### Security Features
- Content protection against copying
- Disabled right-click
- Disabled text selection
- Disabled keyboard shortcuts (Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+U, F12, etc.)
- Disabled developer tools shortcuts
- Disabled drag and drop
- Print protection
- Basic developer tools detection

**Note:** Complete screenshot prevention is technically impossible in web browsers. These measures provide strong discouragement against casual copying attempts.

## Technology Stack

- **Backend:** Django 4.2.7
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5.3
- **Database:** SQLite (development), PostgreSQL-ready
- **Authentication:** Django built-in authentication
- **Forms:** django-crispy-forms with Bootstrap 4


## Security Notes

### Content Protection
The platform implements multiple frontend protection layers:
- CSS user-select: none
- JavaScript event blocking
- Keyboard shortcut disabling
- Right-click prevention
- Developer tools detection

