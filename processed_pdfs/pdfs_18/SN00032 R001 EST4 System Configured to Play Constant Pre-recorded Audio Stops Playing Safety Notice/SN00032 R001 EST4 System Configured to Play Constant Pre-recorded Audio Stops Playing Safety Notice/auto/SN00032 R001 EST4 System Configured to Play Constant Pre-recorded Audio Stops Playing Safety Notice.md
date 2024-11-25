# EST4 System Configured to Play Continuous Pre-recorded Audio Stops Playing  

IMPORTANT SAFETY NOTICE – ACTION REQUIRED  

Please instruct your Sales, Design, Purchasing, Installation, and Service personnel to carefully read this notice and complete the required action.  

# Introduction  

As a responsible manufacturer for fire safety products, product safety is always our first priority. Given their life safety and property protection function, the performance and reliability of our products in your end-use applications are of paramount importance to us.  

You are receiving this Safety Notice because, according to our records, you have purchased a 4-CPU Central Processor Module and 4-AUDTELS Audio IO and Telephone Riser Source Module for your EST4 system where we have identified a potential safety issue when configuring audio riser property settings that may create a potential for personal injury or property damage (see “Issue” below). This Safety Notice also includes “Required actions” on page 2 to correct the potential safety issue that must be adhered to.  

If you are a distributor and/or have sold the potentially affected product (see below) to an end-customer, then we ask that you communicate this information to the potentially affected end-user as described in the instructions provided below.  

# Issue  

An EST4 system can be configured in the 4-CU to play audio messages using one of the audio risers on a 4-AUDTELS installed on a 4-CPU or by using a zone amplifier. While not a recommended configuration, the 4-CU has the option to configure the 4-AUDTELS audio riser as Supervised Out. This configuration is not necessary to supervise the 4-AUDTELS (which is supervised by other means) and instead causes the system to play a continuous 1 kHz tone until a rule is written to play a different message. The system can also be configured to continuously play a pre-recorded message. A safety issue has been identified where if a system uses either of these 4-AUDTELS configurations, because audio played continuously over an extended period of time, it may eventually cause the 4-AUDTELS to time out and not play intended audio messages. When this occurs, the system needs to be restarted to play any audio message.  

This issue was detected in 4-CU firmware version 6.0; however, it is possible that prior versions may also have the same problem. In systems configured with audio riser supervising modules that are supervising the audio signal, the trouble is detected as soon as the issue occurs and any delays have expired.  

Potentially affected products The table below lists products that are potentially affected by the Supervised Out configuration setting.  

<html><body><table><tr><td>Partnumber</td><td>Description</td><td>4-CUfirmwareversion</td></tr><tr><td>4-CPU</td><td>CentralProcessor Module</td><td>Versions6.xandearlier</td></tr></table></body></html>  

# Implemented actions  

Edwards has taken all steps necessary to correct this issue.   
4-CU firmware version 7.0 has removed “Supervised Out” from the Audio Riser configuration options.  

# Required actions  

Given their life safety and/or property protection function, the performance and reliability of our products in enduse applications and/or life safety systems are of paramount importance to us. We expect that this is also of the highest importance to your company. Therefore we ask you to complete the following steps:  

Within 90 days, review your site databases to determine whether any have a 4-CPU node with the Audio Riser x property configured as Supervised Out. If any sites are identified, use the 4-CU to perform the following actions, and then go to the site and download the new database to the control unit.  

1.  For the affected CPU node, change the LRM Configuration, Audio Riser x property from Supervised Out  

to Out. 2.  If audio riser supervision is required, perform the following recommended procedure. a.  Add a TimeControl logic device, and then i.  Set the Hour property to activate every 6 hours. ii.  Set the Duration property to 60 seconds. b.  Add an AudioMessage logic device (example, NCA 1 1 kHz Message), and then i. Download EST4 Wave Files (7351065_01_1kHz_EST4) from the MyEddie website (myeddie.edwardsfiresafety.com) Software page. ii. Attach the downloaded 1kHz_Tone.WAV file to the message. iii. Add the message to your NCA c.  Add an AudioChannel logic device, and then i. Set the Channel Type property to Other. ii. Set the Queue depth property to 1. iii. Add the audio message created above (NCA 1 1 kHz Message) to the channel's message list. iv. Set the channel’s Queue Overflow property to Play Default. v. Set the Default Audio Message property to the audio message that you added to the message list (NCA 1 1 kHz Message). vi.  Add the audio channel to your NCA. d.  If a SIGA-RM1 is used to monitor the audio riser for a signal, configure its fault timer value to 75 seconds. This is required so the module does not go into trouble when no audio message is playing.  

e. Use the following rules example to write a rule for cycling the audio message when Audio Riser x is connected to the amplifier input.  

<html><body><table><tr><td>Startup</td><td>+Delay 05:00 MessageOn 'NCA11KHzMesSage</td></tr><tr><td></td><td>AudioOn '[Node1\HardwareLayer\LRM I1lsPreamplifierl'From 'other Channel'</td></tr><tr><td>TimeControl'ResetAudioTimeControl':AudioOff</td><td>'[Node 1\HardwareLayer\LRM 1jSPreamplifierl'From'Other Channel MessageOff'NCA11KHzMessage</td></tr></table></body></html>  

3. Before turning the audio message back on, ensure no audio message is playing on any of the risers from any channel.  

# Next steps  

1. Review your records to identify the location, quantity, and required actions for the potentially affected products you received from Edwards.   
2. When the remediation schedule is confirmed, update the audio riser setting or upgrade to 4-CU V7.0. You can download “4-CU Version 7.0 Software” from the My-Eddie website. Enter myeddie.edwardsfiresafety.com in your web browser, log in, and then navigate to Resources and Training $>$ Software page.   
3. Visit the affected sites to perform the action in “Required actions” on page 2, within 90 days.   
4. At the site, perform the upgrades on the potentially affected product, as detailed in the “Required actions” on page 2.   
5. Complete the attached “Customer Acknowledgment Form” questions and status of “Required actions” on page 2, for our mutual record keeping purposes.  

# Questions or concerns  

Thank you for your understanding. These measures cannot be conducted successfully without you. The Edwards Customer Service and Technical Support teams, as well as your responsible Account Manager, will be glad to help you with any questions that may arise. Please see “Contact Support” below for contact information.  

# Contact Support  

Tel: +1 800 655 4497 Email contact form: Tech Support Ticket Web: www.edwardsfiresafety.com  