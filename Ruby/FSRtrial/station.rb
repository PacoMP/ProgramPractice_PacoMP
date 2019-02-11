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

#fire = FF.new("Jhon","123@hotmail.com","abcd123","admin",["driver","commander","assistant"],true)
#puts fire.to_s
london = Station.new("BeatleStation","London","392758")
