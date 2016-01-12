from i3pystatus import Status

status = Status(standalone=True)

bar_text_color = "#045B85"
# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b %X",
    hints = {"color":bar_text_color},)

# Shows your CPU temperature, if you have an Intel CPU
status.register("temp",
    format="{temp:.0f} C",
    hints = {"color":bar_text_color},)

# This would look like this:
# Discharging 6h:51m
status.register("battery",
    format="{status} {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS":  "Discharging",
        "CHR":  "Charging",
        "FULL": "Bat full",
    },)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlan0",
    format_up="{essid} {quality:03.0f}%",
    hints = {"color":bar_text_color},)

status.register("network",
    interface = "wlan0",
    format_up = "Down:{bytes_recv:6.1f}KiB Up:{bytes_sent:5.1f}KiB",
    format_down = "",
    dynamic_color = True,
    start_color = bar_text_color,
    end_color = bar_text_color,
    color_down = bar_text_color,
    upper_limit = 800.0,
    )

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="{used}/{total}G [{avail}G]",
    hints = {"color":bar_text_color},)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="Vol: {volume}",
    hints = {"color":bar_text_color},)

status.run()