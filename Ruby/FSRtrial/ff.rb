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
