import sys


prob_Cherry_hyp1 = 1.0
prob_Cherry_hyp2 = 0.75
prob_Cherry_hyp3 = 0.5
prob_Cherry_hyp4 = 0.25
prob_Cherry_hyp5 = 0.0

prior_prob_hyp1 = 0.1
prior_prob_hyp2 = 0.2
prior_prob_hyp3 = 0.4
prior_prob_hyp4 = 0.2
prior_prob_hyp5 = 0.1	

prob_Lime_hyp1 = 0.0
prob_Lime_hyp2 = 0.25
prob_Lime_hyp3 = 0.5
prob_Lime_hyp4 = 0.75
prob_Lime_hyp5 = 1.0

def file_creation():
    
    try:
        file = open("result.txt", 'w')
        print ('File created')
    except:
        print ('Sorry, Cannot create your file!')
    file.write('observation sequence Q: ' + sys.argv[1] +'\n')
    file.write('Length of Q: ' + str(len(sys.argv[1])) +'\n')
    compute(file,sys.argv[1])
    file.close()

def compute(file_output, observation):

	
	flag_var = 0
	temp_a = prior_prob_hyp1
	temp_b = prior_prob_hyp2
	temp_c = prior_prob_hyp3
	temp_d = prior_prob_hyp4
	temp_e = prior_prob_hyp5
	result1 = prob_Cherry_hyp1 * temp_a + prob_Cherry_hyp2 * temp_b + prob_Cherry_hyp3 * temp_c + prob_Cherry_hyp4 * temp_d + prob_Cherry_hyp5 * temp_e
	result2 = 1 - result1
    
	for var in observation:
		flag_var = flag_var + 1
		if var is 'C':
			temp_a = (prob_Cherry_hyp1 * temp_a)/result1
			temp_b = (prob_Cherry_hyp2 * temp_b)/result1
			temp_c = (prob_Cherry_hyp3 * temp_c)/result1
			temp_d = (prob_Cherry_hyp4 * temp_d)/result1
			temp_e = (prob_Cherry_hyp5 * temp_e)/result1
		else:
			temp_a = (prob_Lime_hyp1 * temp_a)/result2
			temp_b = (prob_Lime_hyp2 * temp_b)/result2
			temp_c = (prob_Lime_hyp3 * temp_c)/result2
			temp_d = (prob_Lime_hyp4 * temp_d)/result2
			temp_e = (prob_Lime_hyp5 * temp_e)/result2			
		result1 = prob_Cherry_hyp1 * temp_a + prob_Cherry_hyp2 * temp_b + prob_Cherry_hyp3 * temp_c + prob_Cherry_hyp4 * temp_d + prob_Cherry_hyp5 * temp_e
		result2 =1 - result1
		#can also use result2 = 1 - result1
		print( '\nAfter obs ', flag_var, ' = ', var, ':\n')
		print( 'P(h1 | Q) = ???=> ', temp_a)
		print( 'P(h2 | Q) = ???=> ', temp_b)
		print( 'P(h3 | Q) = ???=> ', temp_c)
		print( 'P(h4 | Q) = ???=> ', temp_d)
		print( 'P(h5 | Q) = ???=> ', temp_e, '\n')
		print( 'Probability that the next candy we pick will be C, given Q: ', result1)
		print( 'Probability that the next candy we pick will be L, given Q: ', result2)
		file_output.write('\nAfter obs ' + str(flag_var) + ' = ' + var + ':\n\n')
		file_output.write('P(h1 | Q) = ???=>' + str(temp_a) + '\n')
		file_output.write('P(h2 | Q) = ???=> ' + str(temp_b) + '\n')
		file_output.write('P(h3 | Q) = ???=> ' + str(temp_c) + '\n')
		file_output.write('P(h4 | Q) = ???=> ' + str(temp_d) + '\n')
		file_output.write('P(h5 | Q) = ???=> ' + str(temp_e) + '\n\n')
		file_output.write('Probability that the next candy we pick will be C, given Q: ' + str(result1) +'\n')
		file_output.write('Probability that the next candy we pick will be L, given Q: ' + str(result2) +'\n')
	
def main():
    print( 'observation sequence Q: ', sys.argv[1])
    print( 'Length of Q: ', len(sys.argv[1]))
    file_creation()
    
if __name__ == "__main__":
	main()