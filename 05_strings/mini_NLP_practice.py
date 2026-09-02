job_ad = """
We are looking for a Python developer.
The candidate should know Python, SQL, Pandas and Git.
Experience with machine learning is a plus.
"""
# Check if the words are in lowercase
print(job_ad.islower())

# convert into lowercase
job_ad_lower = job_ad.lower()

# check if skills appear in the job ad
skills = ["python", "sql", "pandas", "git", "machine learning"]
for skill in skills:
    if skill in job_ad_lower:
        print(f"{skill} is mentioned in the job ad.")
    else:
        print(f"{skill} is NOT mentioned in the job ad.")

# Count how many required skills were found in the job ad
found_skills_count = sum(1 for skill in skills if skill in job_ad_lower)
print(f"Total required skills found in the job ad: {found_skills_count} out of {len(skills)}")

