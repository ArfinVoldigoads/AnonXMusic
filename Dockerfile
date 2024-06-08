FROM nikolaik/python-nodejs:python3.10-nodejs19

# Update and install ffmpeg
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY . /app/
WORKDIR /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Upgrade yt-dlp to the latest version
RUN pip3 install --upgrade yt-dlp

# Set the default command to run your application
CMD bash start
