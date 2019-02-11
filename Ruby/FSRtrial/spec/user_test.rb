require_relative '../app/user'
require 'rspec'

RSpec.describe User do
  it 'has skills' do
    user = User.new('Jhon','pmp@hotmail.com','')
    user.add_skill('Driver')
    expect(user.skills.length).to eq 1
    expect(user.skills).to include 'Driver'
end



  it 'has no rpeated skills' do
    user = User.new('Jhon','pmp@hotmail.com','')
    user.add_skill('Driver')
    user.add_skill('Driver')
    user.add_skill('Commander')
    expect(user.skills.length).to eq 2
    expect(user.skills).to include 'Driver'
    expect(user.skills).to include 'Commander'
  end
#fail "There´s a repeated skill" unless Set.new(user.skills) == user.skills


end
