# canary
PHIOON's Notification system

DESIGN:
  . Develop a ROBUST notification system able to handle notifications in many channels: web_app, email, PUSH (mobile app, when available) and SMS.
  . It is basically an EVENT SYSTEM.
  . It's a new python project. It won't be listening in any other existing project (frontend/backend/website).
  . User should be able to decide what kind of notification they need/want to receive and by which channels in their Profile page (web app).
  . Every notification id must exist in the database with a couple of variables in its text. Examples:
  
    .. notification1: {
        id: "technical_analysis.phitrader.new_position",
        payload: ["asset_symbol", "gain_percentage"],
        email_sender: "notifications@phioon.com",
        amount_retries: 2,
        retry_interval: 10 (minutes)
    }
    .. notification1_email_output: "Hello <<user.first_name>>! Phi Trader just found a new opportunity in the market on asset <<asset_symbol>>.
                                    Potential gain is around <<gain_percentage>>... Come check it out!"
    .. notification1_push_output: "Phi Trader just found a new opportunity in the market on asset <<asset_symbol>>
                                    Potential gain is around <<gain_percentage>>... Come check it out!"
    
    .. notification2: {
        id: "user.subscription.status.past_due",
        payload: ["subscription_label", "renews_on", "automatic_cancel_on"],
        email_sender: "notifications@phioon.com",
        amount_retries: 5,
        retry_interval: 300 (minutes)
    }
    .. notification2_email_output: "Hello <<user.first_name>>! Seems like we had a problem processing your payment for <<subscription_label>> Plan on <<renews_on>>. 
                                    If no payment is made until <<automatic_cancel_on>>, your subscription will be automatically canceled."
    .. notification2_push_output: "Seems like we had a problem processing your payment for <<subscription_label>> Plan on <<renews_on>>.
                                  If no payment is made until <<automatic_cancel_on>>, your subscription will be automatically canceled."
    
    .. If the amount of variables doesn't match with the request's payload, drop the call.
    
  . The system must receive as an input which language id (locale) will be used. If language id is not given or is not expected, drop the call.
  . The actual message text will be stored in files, the same way we currently work with Web App (ptBR.js, enUS.js).  
  . In case of FAILURE trying to send a notification:
    .. Retry accordingly to [retries] notification's field.
    
  . Example of events sent to Canary:
    .. event1: {
        event_id: "user.subscription.status.past_due",
        payload: {
            subscription_label: "Premium",
            renews_on: "2020-11-10",
            automatic_cancel_on: "2020-11-17"
        },
        channels: ["web_app", "email"],
        target_user: {
            first_name: "Jadilson",
            username: "jadilson85",
            email: "jadi_evandro85@gmail.com"
        }
    }
  
  . Canary will have model tables designed to store User's notifications. One table for each notification type:
    .. NotificationWebApp, NotificationPush, NotificationEmail, NotificationSmoke, NotificationMorse...
    
  . Notifications of certain types will have their old entries deleted daily:
    .. web_app: Delete entries older than 60 days.
    .. app_push: Delete entries older than 60 days.
    .. email: Delete entries older than 720 days. Supposing that email notifications are constantly used as formal communications.
    
