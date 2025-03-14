class OSIModel:
    def __init__(self):
        self.layers = [
            "Physical Layer", "Data Link Layer", "Network Layer",
            "Transport Layer", "Session Layer", "Presentation Layer", "Application Layer"
        ]

    def send_data(self, data):
        print("\n=== Sending Data ===")

        print(f"[{self.layers[6]}] Sending message: {data}")
        
        binary_data = ''.join(format(ord(c), '08b') for c in data)
        print(f"[{self.layers[5]}] Encoding to binary: {binary_data}")
        
        print(f"[{self.layers[4]}] Session established.")
        print(f"[{self.layers[3]}] Splitting into segments...")
        print(f"[{self.layers[2]}] Framing data...")
        print(f"[{self.layers[1]}] Preparing frame for transmission...")
        print(f"[{self.layers[0]}] Transmitting bits: {binary_data}")

        print("=== Transmission Complete ===\n")
        return binary_data 

    def receive_data(self, binary_data):
        print("\n=== Receiving Data ===")
        
        print(f"[{self.layers[0]}] Received raw bits: {binary_data}") 
        print(f"[{self.layers[1]}] Processing frame...")
        print(f"[{self.layers[2]}] Routing packet...")
        print(f"[{self.layers[3]}] Reassembling segments...")

        decoded_data = ''.join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
        print(f"[{self.layers[5]}] Decoding binary to text...")
        
        print(f"[{self.layers[6]}] Final received message: {decoded_data}")

        print("=== Reception Complete ===\n")

osi = OSIModel()
binary_data = osi.send_data("Hello")  
osi.receive_data(binary_data)
