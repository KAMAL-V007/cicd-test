# Project 9: Static Site Deployment to S3

## ☁️ The Mission
You have a simple HTML/CSS website. Your goal is to deploy it to an **AWS S3 Bucket** automatically whenever you push code.

## 📂 Project Structure
- `website/`: Contains `index.html` and `style.css`.
- `.github/workflows/`: Where your pipeline lives.

## 📝 The Challenge Requirements

### 1. Simple Build
- **Objective:** Prepare the files.
- **Task:** There is no "build" step for HTML, but imagine there is. Create a step that just lists the files to be deployed (`ls -R website/`).

### 2. Configure AWS Credentials
- **Objective:** Authentication.
- **Task:** Use the `aws-actions/configure-aws-credentials` action.
- You will need to set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION` in your repo secrets.

### 3. Sync to S3
- **Objective:** Deploy.
- **Task:** Use the AWS CLI command to sync the `website/` folder to a bucket.
- Command: `aws s3 sync ./website s3://<your-bucket-name> --delete`

### 4. Invalidate CloudFront (Bonus)
- **Objective:** Clear the cache (if you were using a CDN).
- **Task:** Run a command to print "Invalidating CloudFront cache..." (Simulated).

---

## ⚠️ Prerequisite
You need an AWS Account and an S3 bucket created manually (e.g., `my-cool-site-123`) to actually run this. If you don't have one, just write the workflow and let it fail on the authentication step.
