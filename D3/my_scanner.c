
//sudo docker build . -t scanner_c_test:1.0.0

//sudo docker images

//sudo docker run --rm -it scanner_c_test:1.0.0


#include <libmnl/libmnl.h> //netlink libmnl

#include <linux/nl80211.h> //nl80211 netlink
#include <linux/genetlink.h> //generic netlink
#include <net/if.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>
#include <fcntl.h> //fntnl (set descriptor options)
#include <errno.h> //errno
#include <stdio.h>  //printf
#include <unistd.h> //sleep
#include <time.h>
#include <arpa/inet.h>

#include <linux/netfilter.h>
#include <linux/netfilter/nfnetlink.h>

#ifndef aligned_be64
#define aligned_be64 u_int64_t __attribute__((aligned(8)))
#endif

#include <linux/netfilter/nfnetlink_log.h>

#include <netinet/in.h>
#include <linux/netlink.h>
#include <linux/rtnetlink.h>

int main(int argc, char *argv[])
{
	struct mnl_socket *nl;
	char buf[MNL_SOCKET_BUFFER_SIZE];
	struct nlmsghdr *nlh;
	int ret;
	unsigned int portid, qnum;

	if (argc != 2) { printf("Usage: %s [queue_num]\n", argv[0]); exit(EXIT_FAILURE); }
	qnum = atoi(argv[1]);

	nl = mnl_socket_open(NETLINK_NETFILTER);
	if (nl == NULL) { perror("mnl_socket_open"); exit(EXIT_FAILURE); } 
    
	if (mnl_socket_bind(nl, 0, MNL_SOCKET_AUTOPID) < 0) { perror("mnl_socket_bind"); exit(EXIT_FAILURE); }

	portid = mnl_socket_get_portid(nl); printf("0\n");
    printf("portid = %d\n",portid);
    
	// ----------------------------- function was here ---------------------

	//nlh = nflog_build_cfg_pf_request(buf, NFULNL_CFG_CMD_PF_UNBIND);
	//static struct nlmsghdr *nflog_build_cfg_pf_request(char *buf, uint8_t command)
	uint8_t command = NFULNL_CFG_CMD_PF_UNBIND;
	//struct nlmsghdr *nlh = mnl_nlmsg_put_header(buf);
	nlh = mnl_nlmsg_put_header(buf);
	nlh->nlmsg_type	= (NFNL_SUBSYS_ULOG << 8) | NFULNL_MSG_CONFIG;
	nlh->nlmsg_flags = NLM_F_REQUEST;

	struct nfgenmsg *nfg = mnl_nlmsg_put_extra_header(nlh, sizeof(*nfg));
	nfg->nfgen_family = AF_INET;
	nfg->version = NFNETLINK_V0;

	struct nfulnl_msg_config_cmd cmd = {
		.command = command,
	};
	mnl_attr_put(nlh, NFULA_CFG_CMD, sizeof(cmd), &cmd);
	//return nlh;
	
	printf("nlh->nlmsg_len  = %d\n",nlh->nlmsg_len);
	printf("nlh->nlmsg_type  = %d\n",nlh->nlmsg_type);
	printf("nlh->nlmsg_flags  = %d\n",nlh->nlmsg_flags);
	printf("nlh->nlmsg_seq  = %d\n",nlh->nlmsg_seq);
	printf("nlh->nlmsg_pid  = %d\n",nlh->nlmsg_pid);

	if (mnl_socket_sendto(nl, nlh, nlh->nlmsg_len) < 0) { perror("mnl_socket_send"); exit(EXIT_FAILURE); }

	nlh = nflog_build_cfg_pf_request(buf, NFULNL_CFG_CMD_PF_BIND);
	printf("\n\n nlh->nlmsg_len  = %d\n",nlh->nlmsg_len);
	printf("nlh->nlmsg_type  = %d\n",nlh->nlmsg_type);
	printf("nlh->nlmsg_flags  = %d\n",nlh->nlmsg_flags);
	printf("nlh->nlmsg_seq  = %d\n",nlh->nlmsg_seq);
	printf("nlh->nlmsg_pid  = %d\n",nlh->nlmsg_pid);


	if (mnl_socket_sendto(nl, nlh, nlh->nlmsg_len) < 0) { perror("mnl_socket_send"); exit(EXIT_FAILURE); }

    // ----------------------------- function was here ---------------------

	//nlh = nflog_build_cfg_request(buf, NFULNL_CFG_CMD_BIND, qnum);
	//static struct nlmsghdr * nflog_build_cfg_request(char *buf, uint8_t command, int qnum)
	//uint8_t command = NFULNL_CFG_CMD_BIND;
	command = NFULNL_CFG_CMD_BIND;
	//struct nlmsghdr *nlh = mnl_nlmsg_put_header(buf);
	nlh = mnl_nlmsg_put_header(buf);
	nlh->nlmsg_type	= (NFNL_SUBSYS_ULOG << 8) | NFULNL_MSG_CONFIG;
	nlh->nlmsg_flags = NLM_F_REQUEST;

	//struct nfgenmsg *nfg = mnl_nlmsg_put_extra_header(nlh, sizeof(*nfg));
	nfg = mnl_nlmsg_put_extra_header(nlh, sizeof(*nfg));
	nfg->nfgen_family = AF_INET;
	nfg->version = NFNETLINK_V0;
	nfg->res_id = htons(qnum);

	//struct nfulnl_msg_config_cmd cmd = {
	//	.command = command,
	//};
	cmd.command = command;

	mnl_attr_put(nlh, NFULA_CFG_CMD, sizeof(cmd), &cmd);
	//return nlh;
	

	printf("\n\n nlh->nlmsg_len  = %d\n",nlh->nlmsg_len);
	printf("nlh->nlmsg_type  = %d\n",nlh->nlmsg_type);
	printf("nlh->nlmsg_flags  = %d\n",nlh->nlmsg_flags);
	printf("nlh->nlmsg_seq  = %d\n",nlh->nlmsg_seq);
	printf("nlh->nlmsg_pid  = %d\n",nlh->nlmsg_pid);


	if (mnl_socket_sendto(nl, nlh, nlh->nlmsg_len) < 0) { perror("mnl_socket_send"); exit(EXIT_FAILURE); }

    // ----------------------------- function was here ---------------------

	//nlh = nflog_build_cfg_params(buf, NFULNL_COPY_PACKET, 0xFFFF, qnum);
	//static struct nlmsghdr * nflog_build_cfg_params(char *buf, uint8_t mode, int range, int qnum)
	uint8_t mode = NFULNL_COPY_PACKET;
	int range = 0xFFFF;
	//struct nlmsghdr *nlh = mnl_nlmsg_put_header(buf);
	nlh = mnl_nlmsg_put_header(buf);
	nlh->nlmsg_type	= (NFNL_SUBSYS_ULOG << 8) | NFULNL_MSG_CONFIG;
	nlh->nlmsg_flags = NLM_F_REQUEST;

	//struct nfgenmsg *nfg = mnl_nlmsg_put_extra_header(nlh, sizeof(*nfg));
	nfg = mnl_nlmsg_put_extra_header(nlh, sizeof(*nfg));
	nfg->nfgen_family = AF_UNSPEC;
	nfg->version = NFNETLINK_V0;
	nfg->res_id = htons(qnum);

	struct nfulnl_msg_config_mode params = {
		.copy_range = htonl(range),
		.copy_mode = mode,
	};

	mnl_attr_put(nlh, NFULA_CFG_MODE, sizeof(params), &params);
	//return nlh;
	


	printf("\n\n nlh->nlmsg_len  = %d\n",nlh->nlmsg_len);
	printf("nlh->nlmsg_type  = %d\n",nlh->nlmsg_type);
	printf("nlh->nlmsg_flags  = %d\n",nlh->nlmsg_flags);
	printf("nlh->nlmsg_seq  = %d\n",nlh->nlmsg_seq);
	printf("nlh->nlmsg_pid  = %d\n",nlh->nlmsg_pid);


	if (mnl_socket_sendto(nl, nlh, nlh->nlmsg_len) < 0) { perror("mnl_socket_send"); exit(EXIT_FAILURE); }

    //ret = mnl_cb_run(buf, ret, 0, portid, log_cb, NULL);
	//if (ret < 0){ perror("mnl_cb_run"); exit(EXIT_FAILURE);}
	//printf("ret = %d\n",ret);


    /*
	ret = mnl_socket_recvfrom(nl, buf, sizeof(buf));
	if (ret == -1) { perror("mnl_socket_recvfrom"); exit(EXIT_FAILURE); }
    printf("ret = %d\n",ret);
	while (ret > 0) 
	{
		ret = mnl_cb_run(buf, ret, 0, portid, log_cb, NULL);
		if (ret < 0){ perror("mnl_cb_run -"); exit(EXIT_FAILURE);}
		ret = mnl_socket_recvfrom(nl, buf, sizeof(buf));
		if (ret == -1) { perror("mnl_socket_recvfrom"); exit(EXIT_FAILURE); }
		printf("end\n");
	}
	*/
    
	fprintf(stderr,"========================================== rough work from here ==========================================================================================================================\n");

    nlh = mnl_nlmsg_put_header(buf); // I think this function only assigns the length and leaves other four entries as zero.

	printf("\n\n nlh->nlmsg_len  = %d\n",nlh->nlmsg_len);
	printf("nlh->nlmsg_type  = %d\n",nlh->nlmsg_type);
	printf("nlh->nlmsg_flags  = %d\n",nlh->nlmsg_flags);
	printf("nlh->nlmsg_seq  = %d\n",nlh->nlmsg_seq);
	printf("nlh->nlmsg_pid  = %d\n",nlh->nlmsg_pid);

	nlh->nlmsg_type	= (NFNL_SUBSYS_ULOG << 8) | NFULNL_MSG_CONFIG;
	nlh->nlmsg_flags = NLM_F_REQUEST;

	printf("\n\n nlh->nlmsg_len  = %d\n",nlh->nlmsg_len);
	printf("nlh->nlmsg_type  = %d\n",nlh->nlmsg_type);
	printf("nlh->nlmsg_flags  = %d\n",nlh->nlmsg_flags);
	printf("nlh->nlmsg_seq  = %d\n",nlh->nlmsg_seq);
	printf("nlh->nlmsg_pid  = %d\n",nlh->nlmsg_pid);

    /*
	struct nfgenmsg *nfg1 = mnl_nlmsg_put_extra_header(nlh, sizeof(*nfg1));
	printf("\n\n nfg1->nfgen_family  = %d\n", nfg1->nfgen_family);
	printf("nfg1->version  = %d\n",nfg1->version);
    printf("nfg1->res_id  = %d\n",nfg1->res_id);
	nfg1->nfgen_family = AF_INET;
	nfg1->version = NFNETLINK_V0;
	nfg1->res_id = htons(qnum);
	printf("\n\n nfg1->nfgen_family  = %d\n", nfg1->nfgen_family);
	printf("nfg1->version  = %d\n",nfg1->version);
    printf("nfg1->res_id  = %d\n",nfg1->res_id);
	 */

	uint8_t command1 = NFULNL_CFG_CMD_PF_UNBIND;
	struct nfulnl_msg_config_cmd cmd1 = {
		.command = command1,
	};
	mnl_attr_put(nlh, NFULA_CFG_CMD, sizeof(cmd1), &cmd1);
	
	printf("\n\n nlh->nlmsg_len  = %d\n",nlh->nlmsg_len);
	printf("nlh->nlmsg_type  = %d\n",nlh->nlmsg_type);
	printf("nlh->nlmsg_flags  = %d\n",nlh->nlmsg_flags);
	printf("nlh->nlmsg_seq  = %d\n",nlh->nlmsg_seq);
	printf("nlh->nlmsg_pid  = %d\n",nlh->nlmsg_pid);





	mnl_socket_close(nl);

	return 0;

}

