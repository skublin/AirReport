import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from make_report import make_report


def send_report():
    """
    This is the only one and main function, it takes information about sender and receivers, then sends e-mails with report for last week.
    """
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")

    sender_email = "your@mail.com"
    password = "password"

    receivers = ["receiver-1@mail.com", "receiver-2@mail.com"]

    message = MIMEMultipart("alternative")
    message["Subject"] = f"Weekly report - {today}"
    message["From"] = sender_email

    get_report = make_report(str(today))

    html_www = f"""\
    <html>
        <head>
            <title>Weekly report - {today}</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
                 <br>
                 <div id='plot_PM1'></div>
                 <script>
                     var plotly_data = {get_report['PM1'].to_json()}
                     Plotly.react('plot_PM1', plotly_data.data, plotly_data.layout);
                 </script>
                 <br>
                 <hr>
                 <br>
                 <div id='plot_PM25'></div>
                 <script>
                     var plotly_data = {get_report['PM25'].to_json()}
                     Plotly.react('plot_PM25', plotly_data.data, plotly_data.layout);
                 </script>
                 <br>
                 <hr>
                 <br>
                 <div id='plot_PM10'></div>
                 <script>
                     var plotly_data = {get_report['PM10'].to_json()}
                     Plotly.react('plot_PM10', plotly_data.data, plotly_data.layout);
                 </script>
                 <br>
        </body>
    </html>
    """

    html_mail = f"""\
    <html>
        <head>
        </head>
        <body>
            Hello, leave here your message for e-mail notification.
        </body>
    </html>
    """

    text = MIMEText(html_mail, "html")

    message.attach(text)

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        for receiver in receivers:
            message["To"] = receiver
            server.sendmail(sender_email, receiver, message.as_string())

    with open(f"/path/for/website/{today}.html", 'w') as f:
        f.write(html_www)


if __name__ == "__main__":
    send_report()

