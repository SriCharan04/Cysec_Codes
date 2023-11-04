#Changes pwd to home directory
cd ~

#Uses loop to create folders 1 to 10
for i in {1..10}
do
        mkdir "./$i"
done

#Uses youtube-dl to download the audio content from the video files, with output, in the specified format (without video ID's)
yt-dlp -x --output "~/1/%(title)s.%(ext)s" "https://www.youtube.com/playlist?list=PLc5ZKngbAPXMG4yjq9ESGfqblQfL9g4-p"

#Moves files having y -c haracter in them. Uses pipes to condense the commands into a single line.
ls -R | grep 'y' | xargs -I + mv ./1/+ ./2/+
