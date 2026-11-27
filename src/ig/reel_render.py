import asyncio, subprocess, os
from playwright.async_api import async_playwright
DUR, FPS = 22.0, 30
async def main():
    ff = subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
        "-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-movflags","+faststart","/home/claude/reel/tmp_reel.mp4"],stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto("file:///home/claude/reel/torque_b.html")
        for i in range(int(DUR*FPS)):
            await pg.evaluate(f"render({i/FPS})")
            ff.stdin.write(await pg.screenshot(type="jpeg",quality=92))
        await b.close()
    ff.stdin.close(); r=ff.wait()
    if r==0: os.replace("/home/claude/reel/tmp_reel.mp4","/home/claude/reel/reel-torque.mp4")
    print("ffmpeg", r)
asyncio.run(main())
