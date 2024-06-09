<!DOCTYPE html>
<html>
<head>
    <title>Blue Header Page</title>
    <style>
        header {
            background-color: blue;
            height: 1in; /* 1 inches */
        }
    </style>
</head>
<header>
      <h1>Nhorizon Form</h2>
      <img src="logo.png" width=190px height= 100px alt="Logo" class="logo">

    </header>
<body>
    <header>
        <!-- NewHorizons users -->
    </header>
    
    <main>
Name: <input type="text" name="name" value="<?php echo $name;?>">

E-mail: <input type="text" name="email" value="<?php echo $email;?>">

Website: <input type="text" name="website" value="<?php echo $website;?>">

Comment: <textarea name="comment" rows="5" cols="40"><?php echo $comment;?></textarea>

Gender:
<input type="radio" name="gender"
<?php if (isset($gender) && $gender=="female") echo "checked";?>
value="female">Female
<input type="radio" name="gender"
<?php if (isset($gender) && $gender=="male") echo "checked";?>
value="male">Male

 </header>
    
</body>
</html>
