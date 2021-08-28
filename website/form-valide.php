<?php
$name = $_POST["name"];
$email = $_POST["email"];
$subject = $_POST["subject"];
$message = $_POST["message"];
$gender_male = $_POST["gender"];
$gender_female = $_POST["gender1"];

$email_form = "onfotechsk@gmail.com";

$email_subject = "New Form Submission";

$email_body = "User Name:$name\n",
                "User Email :$email.\n",
                "subject:$subject.\n",
                "message:$message.\n",
                "gender : $gender_male.\n",
                "gender : $gender_female.\n";


$to = "ckarthik55555@gmail.com";

$headers = "from:$email_form \r\n";

$headers .= "Reply-To: $email\r\n";

mail($to,$email_subject,$email_body,$headers);

header("Location : contact.html");

?>
