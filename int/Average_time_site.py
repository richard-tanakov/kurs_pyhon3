minutes, seconds, days = int(input()), int(input()), int(input())

just_seconds = ((minutes * 60) + seconds) * days
hours = just_seconds // 60 // 60
minutes = just_seconds // 60 % 60
seconds = just_seconds % 60
print(hours, minutes, seconds)
