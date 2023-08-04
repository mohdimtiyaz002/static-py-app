# Use the official Nginx image as a base image
FROM nginx:latest

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration to the container
COPY nginx.conf /etc/nginx/conf.d/

# Copy your HTML/CSS files into the container's Nginx web root directory
COPY templates /usr/share/nginx/html/templates
COPY static /usr/share/nginx/html/static

# Expose the port that Nginx is listening on (default is 80)
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]
