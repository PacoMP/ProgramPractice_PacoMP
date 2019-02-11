require 'rubygems'
require 'artii'

class Station

  attr_accessor :name, :city, :address

  def initialize(name,city,address)
    @name = name
    @city = city
    @address = address #Just using ZipCode as address
  end

  def to_s
    "Station: #{@name}, City: #{@city}, Address: #{@address}"

  end

end

#London = Station.new("BeatleStation","London","392758")

class FF

  attr_accessor :name, :email, :password, :roles, :skills, :availabulity

  def initialize (name,email,password,roles,skills,availability)
    @name = name
    @email = email
    @password = password
    @roles = roles #int?
    @skills = skills #array
    @availability = availability #boolean
  end

  def to_s
    "Firefighter: #{@name}
     Email: #{@email}
     Roles: #{@roles}
     Skills #{@skills}
     Availavility; #{@availability}"
  end

end

#fire = FF.new("Jhon","123@hotmail.com","abcd123","admin",["driver","commander","assistant"],true)
#puts fire.to_s
a = Artii::Base.new :font => 'slant'
puts a.asciify('Welcome to FSR!')
