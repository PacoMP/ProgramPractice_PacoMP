class UserDatabase

  attr_accessor :database, :user_id

  def initialize
    @database = []
    @user_id = 0
  end

  def find_by_email(email)
    @database.find { |user| user.email == email }
  end

  def store(user)
    raise 'duplicate user' if find_by_email(user.email)
    @database << user
    user.id = @user_id += 1
  end

  def count
    @database.length
  end

  def all
    @database
  end

  def auth?(email,password)
    true if find_by_email(email).password == password
  end

end
