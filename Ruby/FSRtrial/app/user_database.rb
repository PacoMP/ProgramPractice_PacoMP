class UserDatabase

def initialize
  @database = []
  @user_id = 0
end

def store(user)
  @database << user
  user.id = @user_id += 1
end

def count
  @database.length
end

def all
  @database
end


end
