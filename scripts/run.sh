#!/bin/sh

# Define the application base directory
APP_DIR="/traffic_bot/app"

# Wait for dependent services to be ready (if necessary)
sleep 1

# Load environment variables from the .env file
ENV_FILE=".env"
if [ -e "$ENV_FILE" ]; then
    # Load .env file safely, handling quotes and whitespace
    while IFS='=' read -r key value; do
        # Trim whitespace from the key and value
        key=$(echo "$key" | xargs)
        value=$(echo "$value" | xargs)

        # Skip comments and empty lines
        case "$key" in
            \#* | "") continue ;;
        esac

        # Remove surrounding quotes from the value if present
        value=$(echo "$value" | sed 's/^\(["\'"'"']\)//;s/["\'"'"']$//')

        # Export the variable
        export "$key=$value"
    done < "$ENV_FILE"
    echo "Loaded environment file: $ENV_FILE"
else
    echo "No environment file found at $ENV_FILE. Exiting."
    exit 1
fi
set +a

# Navigate to the application directory
cd "$APP_DIR" || { echo "Failed to change directory to $APP_DIR. Exiting."; exit 1; }

# Database migration
if grep -qi '^ALEMBIC_RUN_MIGRATIONS=True' $ENV_FILE; then
    alembic upgrade head || { echo "Alembic upgrade failed. Exiting."; exit 1; }
fi

# Start the bot
python3.13 -m src.main
