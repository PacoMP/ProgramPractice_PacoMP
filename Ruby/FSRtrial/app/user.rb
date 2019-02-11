class User
require 'set'

  attr_accessor :name, :email, :password, :roles, :skills, :availabulity, :id

  def initialize (name,email,password)
    @name = name
    @email = email
    @password = password
    #@roles = roles #int?
    @skills = Set.new()
    #@availability = availability #boolean
  end

  def to_s
    "Firefighter: #{@name}
     Email: #{@email}
     Roles: #{@roles}
     Skills #{@skills}
     Availavility; #{@availability}"
  end

  def add_skill(skill)
    @skills << skill
  end

end
