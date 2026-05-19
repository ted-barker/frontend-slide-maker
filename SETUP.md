# Setup Instructions for GitHub

Generate branded HTML presentations using AI and design system tokens.

## Creating Private Repo

```bash
cd /Users/ted.barker/Documents/Claude-Skills/projects/frontend-slide-maker

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: Survey Science workshop with Wise branding

- HTML presentation (ready to present)
- Wise brand design system
- Content outline and Google Slides guide
- Complete documentation"

# Create PRIVATE GitHub repo
gh repo create frontend-slide-maker --private --source=. --remote=origin

# Or via web:
# 1. Go to github.com/new
# 2. Name: frontend-slide-maker
# 3. Select: Private
# 4. Do NOT initialize with README (we have one)
# 5. Create repository
# 6. Follow the "push an existing repository" instructions

# Push to GitHub
git push -u origin main
```

## Sharing with Colleagues

Since this is private, colleagues need GitHub access:

**Option 1: Add as Collaborators**
```bash
gh repo edit --add-collaborator colleague-username
```

Or via web: Settings → Collaborators → Add people

**Option 2: Share Files Directly**
- Send `presentation.html` via email/Slack (works standalone)
- Send `wise-brand-kit.json` if they need the brand system

## Keeping Brand Kit Updated

If Wise updates their design system:

```bash
# Update the brand kit file
cp ~/.claude/memory/brands/wise.json ./wise-brand-kit.json

# Commit changes
git add wise-brand-kit.json
git commit -m "Update Wise brand kit"
git push
```

## Security Notes

- ✅ Repo is private - only invited collaborators can see it
- ✅ Brand assets stay within authorized team
- ✅ No public use of Wise branding without approval
- ⚠️ Be careful not to accidentally make repo public later
