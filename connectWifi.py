def connect_wifi():
    import network
    import config

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(config.WIFI_CONFIG['SSID'], config.WIFI_CONFIG['Passphrase'])
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
