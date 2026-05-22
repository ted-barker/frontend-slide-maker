# Git Commit Helper

Intelligently stage files and create well-structured commit messages following best practices.

## Usage

```
/git-commit-helper [--type feat|fix|docs|chore] [--scope name]
```

**Examples:**
- `/git-commit-helper` — Analyze changes and suggest commit
- `/git-commit-helper --type feat --scope auth` — Pre-specify type and scope
- `/git-commit-helper --amend` — Amend previous commit

## What It Does

1. **Analyzes Git Status**
   - Lists all modified, added, deleted files
   - Shows line changes per file
   - Categorizes files by type

2. **Suggests Staging Strategy**
   - ✅ Include: Source code, docs, configs
   - ⚠️ Review: Large files, generated files
   - ❌ Exclude: Build artifacts, temp files, secrets

3. **Validates Changes**
   - Check for secrets (API keys, tokens, passwords)
   - Detect large files (>1MB)
   - Find debug code (console.log, debugger, pdb)
   - Verify .gitignore patterns

4. **Generates Commit Message**
   - Follows Conventional Commits format
   - Extracts change summary from diffs
   - Suggests type (feat/fix/docs/chore/refactor/test)
   - Lists key changes in body

5. **Executes Commit**
   - Stages suggested files
   - Creates commit with generated message
   - Adds co-author attribution

## Workflow

### Step 1: Analyze Repository State

```bash
git status --porcelain
git diff --stat
git diff --cached --stat
```

Categorize files:
- **Source**: .js, .ts, .py, .go, .rs, .java, etc.
- **Docs**: .md, .txt, .rst, docs/
- **Config**: package.json, .gitignore, .env.example, tsconfig.json
- **Tests**: .test.js, .spec.ts, test/, __tests__/
- **Build**: dist/, build/, .next/, target/
- **Temp**: .DS_Store, *.log, .cache/, node_modules/
- **IDE**: .vscode/, .idea/, *.swp

### Step 2: Show Analysis

Present to user:

```
📊 Git Status Analysis

Modified Files (5):
✓ src/auth/login.ts (48 lines added, 12 deleted)
✓ src/auth/types.ts (15 lines added)
✓ README.md (23 lines added)
⚠️ src/utils/debug.ts (contains console.log statements)
❌ dist/bundle.js (build artifact - should be gitignored)

Untracked Files (3):
✓ tests/auth.test.ts (new test file)
⚠️ .env.local (local config - check for secrets)
❌ node_modules/ (dependency directory - should be gitignored)

Staging Suggestion:
  Include (4 files):
    src/auth/login.ts
    src/auth/types.ts
    README.md
    tests/auth.test.ts
  
  Review (1 file):
    src/utils/debug.ts (contains debug code)
  
  Exclude (2 files):
    dist/bundle.js (add to .gitignore)
    .env.local (add to .gitignore)
    node_modules/ (already in .gitignore)

Validations:
⚠️ Warning: src/utils/debug.ts contains console.log (line 42)
⚠️ Warning: .env.local might contain secrets

Proceed with staging? (yes/edit/cancel)
```

### Step 3: Generate Commit Message

Analyze diffs to determine:

**Commit Type:**
- `feat`: New feature or functionality added
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Formatting, missing semi-colons, etc (no code change)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding or updating tests
- `chore`: Updating build tasks, package manager, etc

**Commit Scope:**
- Extract from file paths (e.g., `auth`, `api`, `ui`, `db`)
- Ask user if ambiguous

**Subject Line:**
- Imperative mood ("add" not "added" or "adds")
- No capitalization
- No period at end
- Max 50 characters
- Summarize the "what" not the "how"

**Body:**
- Bullet points for multiple changes
- Explain "why" if not obvious
- Reference issues/tickets if applicable

**Example Generated Message:**

```
feat(auth): add OAuth2 login flow

- Implement OAuth2 authentication with Google provider
- Add token refresh mechanism
- Create auth types and interfaces
- Update README with OAuth setup instructions

Closes #123
```

### Step 4: Review and Edit

Show generated message:

```
Proposed Commit Message:

feat(auth): add OAuth2 login flow

- Implement OAuth2 authentication with Google provider
- Add token refresh mechanism
- Create auth types and interfaces
- Update README with OAuth setup instructions

Options:
• "commit" - Create commit with this message
• "edit" - Modify the message
• "change type to fix" - Change commit type
• "change scope to api" - Change scope
• "cancel" - Abort commit
```

### Step 5: Execute Commit

```bash
# Stage approved files
git add src/auth/login.ts src/auth/types.ts README.md tests/auth.test.ts

# Create commit
git commit -m "feat(auth): add OAuth2 login flow

- Implement OAuth2 authentication with Google provider
- Add token refresh mechanism
- Create auth types and interfaces
- Update README with OAuth setup instructions

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

Confirm:
```
✓ Commit created: abc1234
✓ 4 files staged and committed

Next steps:
• Push to remote: git push origin main
• View commit: git show
• Amend if needed: /git-commit-helper --amend
```

## Validation Rules

### Secret Detection Patterns

Check for patterns in diffs:
```regex
API[_-]?KEY\s*=\s*["']?[\w-]+["']?
SECRET[_-]?KEY\s*=\s*["']?[\w-]+["']?
PASSWORD\s*=\s*["']?[\w-]+["']?
TOKEN\s*=\s*["']?[\w-]+["']?
aws_access_key_id
private[_-]?key
```

If found:
```
🚨 Potential Secret Detected!

File: config/settings.py
Line 42: API_KEY = "sk-1234567890abcdef"

This looks like an API key. Do NOT commit this file.

Suggestions:
• Move secret to .env file
• Add .env to .gitignore
• Use environment variables
• Remove secret from code
```

### Large File Detection

Files >1MB:
```
⚠️ Large File Detected

File: assets/video.mp4 (15.2 MB)

Large files should not be committed to Git.

Suggestions:
• Use Git LFS: git lfs track "*.mp4"
• Store in external storage (S3, CDN)
• Add to .gitignore if not needed
• Compress if possible
```

### Debug Code Detection

Patterns:
```regex
console\.(log|debug|info|warn|error)
debugger;
print\(
pdb\.set_trace\(\)
println!
fmt\.Println
```

If found:
```
⚠️ Debug Code Found

File: src/utils/helper.ts
Line 42: console.log('Debug:', data);

Remove debug statements before committing.

Options:
• Remove manually and re-stage
• Continue anyway (not recommended)
• Skip this file
```

## File Categorization Logic

### Always Include
- Source code files being tracked
- Documentation updates
- Configuration that's shared (.gitignore, package.json)
- Tests

### Always Exclude
- Build artifacts (dist/, build/, *.pyc, *.class)
- Dependencies (node_modules/, vendor/, venv/)
- IDE settings (.vscode/, .idea/, *.swp) unless team-shared
- OS files (.DS_Store, Thumbs.db)
- Log files (*.log, logs/)
- Local config (.env, .env.local, secrets.json)
- Temporary files (tmp/, cache/, *.tmp)

### Review Required
- New binary files
- Files >100KB
- Files with "temp" or "test" in name (might be disposable)
- Files outside typical project structure

## Conventional Commits Reference

Format:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting (no functional change)
- `refactor`: Code restructuring (no behavior change)
- `perf`: Performance improvement
- `test`: Tests
- `build`: Build system or dependencies
- `ci`: CI configuration
- `chore`: Maintenance
- `revert`: Revert previous commit

**Scopes (examples):**
- `auth`, `api`, `ui`, `db`, `config`, `deps`

**Breaking Changes:**
```
feat(api)!: change authentication endpoint

BREAKING CHANGE: /auth endpoint now requires OAuth2
```

## Advanced Features

### Suggest .gitignore Additions

If excluded files aren't in .gitignore:

```
💡 Suggested .gitignore Updates

Add these entries to .gitignore:

# Build artifacts
dist/
build/

# Environment
.env.local

# OS files
.DS_Store

Add to .gitignore? (yes/no)
```

### Atomic Commit Detection

If changes span multiple concerns:

```
⚠️ Non-Atomic Commit Detected

Your changes include:
• New auth feature (src/auth/)
• Bug fix in API (src/api/fix.ts)
• Documentation update (README.md)

Suggestion: Split into separate commits:

Commit 1 (feat): Auth changes
  src/auth/login.ts
  src/auth/types.ts

Commit 2 (fix): API bug fix
  src/api/fix.ts

Commit 3 (docs): README update
  README.md

Split commits? (yes/no/continue)
```

### Co-Author Support

If pair programming:

```
Add co-authors? (yes/no)

Co-Authored-By: Jane Smith <jane@example.com>
Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
```

## Progressive Disclosure

Load resources on-demand:

- **SKILL.md** (this file) — Core workflow
- **resources/secret-patterns.json** — Secret detection rules
- **resources/gitignore-templates.md** — Common .gitignore patterns
- **resources/commit-types.md** — Detailed commit type guidance
- **resources/file-categories.json** — File type categorization rules

## Instructions for Claude

When this skill is invoked:

1. **Check Git repository**:
   ```bash
   git rev-parse --git-dir 2>/dev/null
   ```
   If not a git repo: "Not a git repository. Run `git init` first."

2. **Get repository state**:
   ```bash
   git status --porcelain
   git diff --stat
   git diff --cached --stat
   ```

3. **Analyze each file**:
   - Categorize by type (source/docs/config/build/temp)
   - Check size (`ls -lh`)
   - Check for secrets (pattern matching)
   - Check for debug code (pattern matching)
   - Determine if tracked or untracked

4. **Generate staging suggestion**:
   - Include: Source, docs, tests, shared config
   - Exclude: Build artifacts, temp files, secrets
   - Review: Large files, debug code, new binaries

5. **Show analysis** to user with categorized files

6. **Wait for confirmation**:
   - "yes" → Continue to commit message generation
   - "edit" → Let user modify file selection
   - "cancel" → Abort

7. **Generate commit message**:
   - Read diffs to understand changes
   - Determine commit type (feat/fix/docs/etc)
   - Extract scope from file paths
   - Write subject line (imperative, <50 chars)
   - Write body with bullet points
   - Add co-author footer

8. **Show proposed message** and wait for approval

9. **Execute commit**:
   ```bash
   git add <files>
   git commit -m "<message>"
   ```

10. **Confirm completion** and suggest next steps

## Best Practices

- **One logical change per commit**
- **Write for humans** - commits are communication
- **Be specific** - "fix login bug" not "fix bug"
- **Explain why** - not just what
- **Reference issues** - "Closes #42" or "Fixes #123"
- **Test before committing** - ensure code works
- **Review diffs** - use `git diff` before committing
- **Atomic commits** - easy to revert, review, cherry-pick

## Error Handling

**No changes to commit:**
```
No changes detected. Working directory is clean.
```

**Merge conflict:**
```
⚠️ Merge Conflict Detected

Resolve conflicts before committing:
  src/auth/login.ts (both modified)

Resolve and re-run /git-commit-helper
```

**Detached HEAD:**
```
⚠️ Detached HEAD State

You're not on a branch. Create or checkout a branch first:
  git checkout -b feature/new-feature
  git checkout main
```

## Example Sessions

### Session 1: Feature Commit

```
User: /git-commit-helper

Claude:
📊 Git Status Analysis

Modified (2):
✓ src/auth/oauth.ts (120 lines added)
✓ README.md (15 lines added)

New (1):
✓ tests/auth.test.ts (new file)

Staging all 3 files.

Proposed Message:
feat(auth): add OAuth2 login flow

- Implement OAuth2 with Google provider
- Add token refresh mechanism
- Update README with OAuth setup

Commit? (yes/edit)

User: yes

Claude:
✓ Commit created: abc1234
✓ 3 files committed

Next: git push origin main
```

### Session 2: Multiple Concerns (Split Suggested)

```
User: /git-commit-helper

Claude:
⚠️ Non-Atomic Commit Detected

Changes span 2 concerns:
1. Auth feature (src/auth/)
2. API bug fix (src/api/)

Recommend splitting into 2 commits.

Split? (yes/no)

User: yes

Claude:
Commit 1/2: Auth feature

Files:
✓ src/auth/oauth.ts
✓ tests/auth.test.ts

Message:
feat(auth): add OAuth2 login

Commit this? (yes)

User: yes

Claude:
✓ Commit 1 created: abc1234

Commit 2/2: API bug fix

Files:
✓ src/api/users.ts

Message:
fix(api): handle null user IDs

Commit this? (yes)

User: yes

Claude:
✓ Commit 2 created: def5678
✓ All changes committed (2 commits)
```

## Notes

- Compatible with any Git repository
- Works with GitHub, GitLab, Bitbucket, etc.
- Follows industry best practices
- Configurable via project .gitcommithelper.json (future feature)
- Integrates with Git hooks (pre-commit, commit-msg)
