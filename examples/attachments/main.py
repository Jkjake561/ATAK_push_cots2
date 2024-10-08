from atakcots import CotConfig, CotServer

if __name__ == "__main__":
    # Configure the COT message details (UID, coordinates, and optional attachment)
    cot_config = CotConfig(
        uid="Message",  # Unique identifier for the COT message
        latitude=40.74931973338903,  # Example latitude (New York City)
        longitude=-73.96791282024928,  # Example longitude (New York City)
        attachment_paths="sandeot.png"  # Example image attachment (can be None)
    )
        
    # Configure CotServer to send the message to localhost (127.0.0.1) on UDP port 4242
    with CotServer("127.0.0.1", 8000) as server:
        # Send the COT message to localhost (127.0.0.1), port 4242
        server.push_cot(cot_config, "127.0.0.1")
        print("COT message sent to WinTAK/ATAK at localhost (127.0.0.1) on port 4242")

    # Keep the script running to maintain the server state
    while True:
        pass
