import requests

def get_roblox_user_data(username):
    # Получаем данные пользователя
    user_response = requests.get(f"https://api.roblox.com/users/get-by-username?username={username}")
    if user_response.status_code == 200:
        user_data = user_response.json()
        user_id = user_data["Id"]
        
        # Получаем аватарку
        avatar_response = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png")
        avatar_data = avatar_response.json()
        avatar_url = avatar_data["data"][0]["imageUrl"]
        
        return {
            "username": user_data["Username"],
            "user_id": user_id,
            "avatar_url": avatar_url
        }
    return None

# Пример использования
user_info = get_roblox_user_data("Roblox")
print(user_info)