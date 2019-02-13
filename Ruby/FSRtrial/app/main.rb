require 'rubygems'
require 'artii'
require 'faker'

require_relative 'user'
require_relative 'user_database'
require_relative 'station'

def loggedin_menu
  input = ''
  while input != '1' && input != '2' && input != '3'
  puts 'What would you like to do?:'
  puts '1.- Search by \'keyword\''
  puts '2.- Add skills'
  puts '3.- Look/Change availability'
  input = gets.chomp
  end

  case input
  when '1' then
    puts 'This should search by keyword'
  when '2' then
    add_skills
  when '3' then
    puts 'This should change availability'
  end

end

def add_skills
  skills_database = ['Driver', 'Commander', 'Normal ff', 'Diver', 'LT driver']

  input = ''
  while input != 'Exit'
    puts 'Select skills from the list to add'
    skills_database.each_with_index do |skill,index|
      puts  "#{index} .- #{skill}"
    end
    puts 'Exit'
    input = gets.chomp.to_i
    puts input
    if input.is_a? Numeric #&& is in range ()
      puts skills_database[input.to_i]
      @current_user.input_skill(skills_database[input.to_i])
    else
      puts 'Invalid character '
    end

  end

  puts @current_user
end

user_database = UserDatabase.new

5.times do
  complete_name = (Faker::Name.first_name) + ' ' + (Faker::Name.last_name)
  user_database.store(User.new(complete_name, Faker::Internet.email, ''))
end

puts user_database.database

a = Artii::Base.new :font => 'slant'
puts a.asciify('Welcome to FSR!')


input = ''
while input != '1' && input != '2' && input != '3'
  puts 'Please select one of the following options:'
  puts '1.- User Log in'
  puts '2.- New User'
  puts '3.- Search by \'keyword\''
  input = gets.chomp
end

case input
when '1' then
  puts 'Please enter your email'
  email = gets.chomp
  puts 'Please enter your password'
  password = gets.chomp

  if @current_user = user_database.authenticate(email,password)
    puts "Login successful"
    loggedin_menu
  else
    puts 'Your email or password do not match'
  end

when '2' then
  puts 'Enter your name to register'
  new_name = gets.chomp
  puts 'Enter and email to associate to your account'
  new_email = gets.chomp
  puts 'Enter a password for your new account'
  new_password = gets.chomp

  if user_database.store(User.new(new_name,new_email,new_password))
    puts "#{user_database.find_by_email(new_email).name} your account with the email #{user_database.find_by_email(new_email).email} has been created succesfully!"
  else
    puts "This email is already registered"
  sleep(5)
  end
  #puts user_database.database
end





#z.each {|i| print food + ' '}
