def create_youtube_video(title, description):
    ytvid = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}  # Using an empty dictionary for comments
    }
    return ytvid

def like(ytvid):
    if 'likes' in ytvid:
        ytvid['likes'] += 1
    return ytvid

def dislike(ytvid):
    if 'dislikes' in ytvid:
        ytvid['dislikes'] += 1
    return ytvid

def add_comment(ytvid, username, comment_text):
    ytvid['comments'][username] = comment_text
    return ytvid

youtube_video = create_youtube_video("Trisha Paytas Mukbang", "Trisha eating buldak noodles")
print(youtube_video)

youtube_video = like(youtube_video)
print(youtube_video)

youtube_video = dislike(youtube_video)
print(youtube_video)

youtube_video = add_comment(youtube_video, "User1", "Great video!")
youtube_video = add_comment(youtube_video, "User2", "Love it!")
print(youtube_video)
