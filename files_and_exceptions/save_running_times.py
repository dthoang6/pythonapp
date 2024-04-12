# This program saves a sequence of video running times to the video_times.txt

def save_running_time():
  outfile = open('video_times.txt', 'w')
  number_videos = int(input('Enter number of videos to record running time: '))

  for video in range(1, number_videos + 1):
    video_running_time = input('Enter the running time of video #' + str(video) + ': ')
    outfile.write(video_running_time + '\n')

  outfile.close()

# the read_running_times function to read the string value in video_times.txt
# then calculate the total time
def read_running_times():
  video_file = open('video_times.txt', 'r')
  total = 0.0   # Initialize an accumulator to 0.00
  count = 0     # Initialize a variable to keep count of the videos

  for line in video_file:
    # Convert a line to a float
    run_time = float(line)
    count += 1
    total += run_time
    # Display the time for each video
    print('Video #', count, ': ', run_time, sep='')
  
  video_file.close()
  print('The total running time is', total, 'seconds.')

def main():
  read_running_times()
main()