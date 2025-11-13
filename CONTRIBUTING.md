# Contributing to Anachak Kasekor Chatbot

First off, thank you for considering contributing to Anachak Kasekor Chatbot! It's people like you that make this project better for farmers across Cambodia.

## 🌾 Code of Conduct

By participating in this project, you are expected to uphold our values of respect, collaboration, and dedication to helping farmers.

## 🚀 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if possible**
- **Note your environment** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other projects**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code, ensure it follows our coding standards
3. Test your changes thoroughly
4. Update documentation as needed
5. Write clear commit messages
6. Submit your pull request

## 💻 Development Process

### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Anachak-Kasekor-Chatbot.git
cd Anachak-Kasekor-Chatbot

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add your test bot token
```

### Coding Standards

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Write docstrings for functions and classes

### Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when relevant

Examples:
```
Add weather alert feature
Fix soil detection button link
Update README with new installation steps
```

### Branch Naming

- `feature/` - New features (e.g., `feature/add-crop-recommendation`)
- `fix/` - Bug fixes (e.g., `fix/button-redirect-issue`)
- `docs/` - Documentation updates (e.g., `docs/update-readme`)
- `refactor/` - Code refactoring (e.g., `refactor/optimize-image-loading`)

## 🧪 Testing

Before submitting your pull request:

1. Test the bot manually with `/start` command
2. Verify all buttons work correctly
3. Check both Khmer and English language options
4. Ensure no errors in console output

## 📝 Documentation

- Update README.md if you change functionality
- Add comments to complex code sections
- Update .env.example if you add new environment variables

## 🤝 Community

- Be respectful and constructive
- Help others when you can
- Share your knowledge
- Celebrate successes together

## ❓ Questions?

Feel free to open an issue with the `question` label or contact the team directly.

---

Thank you for contributing to make farming smarter and easier for Cambodian farmers! 🌾
