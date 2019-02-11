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

  end

  it 'is not adding duplicate emails' do

  end

end
