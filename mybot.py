import time
from post import post_new_video

def main():
    
    post_new_video()

if __name__ == '__main__':
    while True:
        main()
        # 1 hour break
        time.sleep(1*1)
