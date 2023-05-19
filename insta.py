import instaloader
insta = instaloader . Instaloader()
dp = input("Enter instagram username: ")
insta.download_profile(dp, profile_pic_only=True)