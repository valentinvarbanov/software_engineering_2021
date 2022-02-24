# Choose a base image to start from
FROM ubuntu:latest

# Install dependancies
RUN apt-get update && apt-get install -y g++

# Copy main.cpp inside the container
COPY . .

# Compile the main.cpp
RUN g++ main.cpp 

# Specify the starting point for `docker run`
CMD [ "./a.out" ]