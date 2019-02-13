require_relative '../app/user'
require_relative '../app/user_database'
require 'rspec'


RSpec.describe UserDatabase do
  it 'creates users' do
    user_database = UserDatabase.new
    new_user = User.new('Jhon','pmp@hotmail.com','')
    user_database.store(new_user)
    expect(user_database.count).to eq 1
    expect(user_database.all).to include new_user
  end

  it 'assigns a unique ID to users' do
    user_database = UserDatabase.new
    user1 = User.new('Jhon','pmp@hotmail.com','')
    user2 = User.new('Paco','paco@hotmail.com','')

    user_database.store(user1)
    user_database.store(user2)

    expect(user1.id).to eq 1
    expect(user2.id).to eq 2
  end

  it 'finds users by email' do
    user_database = UserDatabase.new
    user1 = User.new('Jhon','pmp@hotmail.com','')
    user_database.store(user1)
    user_by_email = user_database.find_by_email('pmp@hotmail.com')
    expect(user_by_email.email).to eq user1.email
  end

  it 'is not adding duplicate emails' do
    user_database = UserDatabase.new
    user1 = User.new('Jhon','pmp@hotmail.com','')
    user_database.store(user1)

    user2 = User.new('Hank','pmp@hotmail.com','')
    expect { user_database.store(user2) }.to raise_error
    expect(user_database.count).to eq 1
  end

  it 'authenticates user' do
    user_database = UserDatabase.new
    user1 = User.new('Jhon','pmp@hotmail.com','password')
    user_database.store(user1)

    expect(user_database.authenticate(user1.email,user1.password)).to eq user1
  end

  it 'does not authenticate user with incorrect credentials' do
    user_database = UserDatabase.new
    user1 = User.new('Jhon','pmp@hotmail.com','password')
    user_database.store(user1)

    expect(user_database.authenticate(user1.email, "incorrect")).to eq nil
  end


    it 'does not authenticate user with non existing email' do
      user_database = UserDatabase.new
      user1 = User.new('Jhon','pmp@hotmail.com','password')
      user_database.store(user1)

      expect(user_database.authenticate("does@not.exist", user1.password)).to eq nil
    end
end
