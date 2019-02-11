require 'rubygems'
require 'artii'
require 'faker'

require_relative 'ff'
require_relative 'station'

ffs = []
5.times do
  complete_name = (Faker::Name.first_name) + " " + (Faker::Name.last_name)
  ffs.append(FF.new(complete_name,Faker::Internet.email,'','',[],''))
end

puts ffs

a = Artii::Base.new :font => 'slant'
puts a.asciify('Welcome to FSR!')


input = ''
while input != '1' && input != '2' && input != '3'
  puts "Please select one of the following options:"
  puts "1.- User Log in"
  puts "2.- New User"
  puts "3.- Search by \"keyword\""
  input = gets.chomp
end

case input
when '1' then
  email_flag = false
  password_flag = false
  puts "Please enter your email"
  email = gets.chomp
  puts "Please enter your password"
  password = gets.chomp

  ffs.each {|ff|
          email_flag = true if ff.email == email
          password_flag = true if ff.password == password
            }

  if email_flag == true && password_flag == true
    puts "Login successful!!!"
  else
    puts "Your email and/or password do not match"
  end

when '2' then
  puts "Enter your name to register"
  new_name = gets.chomp
  puts "Enter and email to associate to your account"
  new_email = gets.chomp
  puts "Enter a password for your new account"
  new_password = gets.chomp
  ffs.append(FF.new(new_name,new_email,new_password,'',[],''))
  puts "#{ffs[-1].name} your account with the email #{ffs[-1].email} has been created succesfully!"
  sleep(5)
  puts ffs
end





#z.each {|i| print food + " "}
