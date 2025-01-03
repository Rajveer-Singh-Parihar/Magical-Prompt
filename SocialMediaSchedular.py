import datetime
import json
import os
from datetime import datetime, timedelta

class Post:
    def __init__(self, content, platform, scheduled_time):
        self.content = content
        self.platform = platform
        self.scheduled_time = scheduled_time
        self.status = "scheduled"  # scheduled, posted, failed
        self.id = datetime.now().strftime("%Y%m%d%H%M%S")

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "platform": self.platform,
            "scheduled_time": self.scheduled_time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status
        }

class SocialMediaScheduler:
    def __init__(self):
        self.posts = []
        self.platforms = ["Twitter", "Facebook", "Instagram", "LinkedIn"]
        self.data_file = "scheduled_posts.json"
        self.load_posts()

    def load_posts(self):
        """Load previously scheduled posts from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    posts_data = json.load(file)
                    for post_data in posts_data:
                        post = Post(
                            post_data["content"],
                            post_data["platform"],
                            datetime.strptime(post_data["scheduled_time"], "%Y-%m-%d %H:%M:%S")
                        )
                        post.id = post_data["id"]
                        post.status = post_data["status"]
                        self.posts.append(post)
            except json.JSONDecodeError:
                print("Error loading posts file. Starting with empty schedule.")

    def save_posts(self):
        """Save scheduled posts to file"""
        posts_data = [post.to_dict() for post in self.posts]
        with open(self.data_file, 'w') as file:
            json.dump(posts_data, file, indent=2)

    def schedule_post(self, content, platform, scheduled_time):
        """Schedule a new post"""
        if platform not in self.platforms:
            raise ValueError(f"Invalid platform. Choose from: {', '.join(self.platforms)}")
        
        if len(content) > 280 and platform == "Twitter":
            raise ValueError("Twitter posts cannot exceed 280 characters")

        post = Post(content, platform, scheduled_time)
        self.posts.append(post)
        self.save_posts()
        return post.id

    def view_scheduled_posts(self):
        """View all scheduled posts"""
        return sorted(self.posts, key=lambda x: x.scheduled_time)

    def delete_post(self, post_id):
        """Delete a scheduled post"""
        self.posts = [post for post in self.posts if post.id != post_id]
        self.save_posts()

    def edit_post(self, post_id, new_content=None, new_platform=None, new_time=None):
        """Edit a scheduled post"""
        for post in self.posts:
            if post.id == post_id:
                if new_content is not None:
                    if new_platform == "Twitter" and len(new_content) > 280:
                        raise ValueError("Twitter posts cannot exceed 280 characters")
                    post.content = new_content
                if new_platform is not None:
                    if new_platform not in self.platforms:
                        raise ValueError(f"Invalid platform. Choose from: {', '.join(self.platforms)}")
                    post.platform = new_platform
                if new_time is not None:
                    post.scheduled_time = new_time
                self.save_posts()
                return True
        return False

def main():
    scheduler = SocialMediaScheduler()
    
    while True:
        print("\nSocial Media Scheduler")
        print("1. Schedule new post")
        print("2. View scheduled posts")
        print("3. Edit post")
        print("4. Delete post")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            content = input("Enter post content: ")
            print("\nAvailable platforms:", ", ".join(scheduler.platforms))
            platform = input("Enter platform: ")
            date_str = input("Enter scheduled time (YYYY-MM-DD HH:MM): ")
            try:
                scheduled_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                post_id = scheduler.schedule_post(content, platform, scheduled_time)
                print(f"Post scheduled successfully! ID: {post_id}")
            except (ValueError, Exception) as e:
                print(f"Error: {str(e)}")

        elif choice == "2":
            posts = scheduler.view_scheduled_posts()
            if not posts:
                print("No scheduled posts.")
            else:
                print("\nScheduled Posts:")
                for post in posts:
                    print(f"\nID: {post.id}")
                    print(f"Platform: {post.platform}")
                    print(f"Scheduled Time: {post.scheduled_time}")
                    print(f"Status: {post.status}")
                    print(f"Content: {post.content}")

        elif choice == "3":
            post_id = input("Enter post ID to edit: ")
            new_content = input("Enter new content (press Enter to skip): ") or None
            new_platform = input("Enter new platform (press Enter to skip): ") or None
            new_time_str = input("Enter new time YYYY-MM-DD HH:MM (press Enter to skip): ")
            new_time = None if not new_time_str else datetime.strptime(new_time_str, "%Y-%m-%d %H:%M")
            
            try:
                if scheduler.edit_post(post_id, new_content, new_platform, new_time):
                    print("Post updated successfully!")
                else:
                    print("Post not found.")
            except ValueError as e:
                print(f"Error: {str(e)}")

        elif choice == "4":
            post_id = input("Enter post ID to delete: ")
            scheduler.delete_post(post_id)
            print("Post deleted successfully!")

        elif choice == "5":
            print("Thank you for using Social Media Scheduler!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()