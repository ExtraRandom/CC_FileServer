import subprocess
import os


def update_ytdl():
    cmd = "python -m pip install -U yt-dlp"
    subprocess.call(cmd.split(" "))
    return


def search_and_get_id(search):
    cmd = ["yt-dlp", f"ytsearch:{search}", "--print", "id"]
    out = subprocess.check_output(cmd, shell=False)
    return str(out.decode()).strip()


def download_audio(url, v_id):
    """take search term and download first result"""
    folder = os.path.join(os.getcwd(), "audio")
    outtmpl = os.path.join(folder, "{}.%(ext)s".format(v_id))

    mp3_file = os.path.join(folder, f"{v_id}.mp3")
    cc_file = os.path.join(folder, f"{v_id}.dfpwm")

    if os.path.exists(cc_file) is False:
        # cmd = ["yt-dlp", f"ytsearch:{search}",
        # "-f", "bestaudio", "--extract-audio", "--audio-format", "mp3", "-o", outtmpl]
        cmd = f"yt-dlp -o {outtmpl} --extract-audio --audio-format mp3 {url}"
        subprocess.call(cmd, shell=False)
        print("download done, onto processing")
        ffmpeg = f'ffmpeg -n -i "{mp3_file}" -ac 1 -c:a dfpwm "{cc_file}" -ar 48k'
        subprocess.call(ffmpeg, shell=False)

        os.remove(mp3_file)

    return f"{v_id}.dfpwm"





