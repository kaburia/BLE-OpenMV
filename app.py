from flask import Flask, render_template, request
import asyncio
import bleak

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pair', methods=['POST'])
async def pair_device():
    device_address = request.form.get('device_address')

    # Pairing logic using bleak
    devices = await bleak.discover()
    target_device = None
    for device in devices:
        if device.address == device_address:
            target_device = device
            break

    if target_device:
        async with bleak.BleakClient(target_device) as client:
            # Perform pairing process
            await client.pair()

            # Display the paired device information
            paired_info = {
                'Name': target_device.name,
                'Address': target_device.address
                # Add more device information fields as needed
            }

    return render_template('paired.html', paired_info=paired_info)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.ensure_future(app.run_asyncio()))
